# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
from odoo.addons.crm.models.crm_lead import Lead

_logger = logging.getLogger(__name__)

class ChecklistItem(models.Model):
    _name = 'crm.lead.checklist.item'
    _description = 'Entry on a lead checklist'
    _sql_constraints = [
        ('uniq_name', 'unique(name)', "A item with this name exists already")
    ]

    name = fields.Char(required=True, translate=True)

class Checklist(models.Model):
    _inherit = 'crm.lead'

    progress = fields.Integer(compute='_compute_progress')

    checklist_item_ids = fields.Many2many(
        'crm.lead.checklist.item', 'crm_lead_checklist_rel', 'lead_id', 'checklist_item_id',
        string="Checklist Items", tracking=True
    )

    def _compute_progress(self):
        for rec in self:
            fin_items = len(rec.checklist_item_ids)
            max_items = len(self.env['crm.lead.checklist.item'].search([]))
            rec.progress = 100 * fin_items / max_items

    @api.onchange('checklist_item_ids')
    def _onchange_checklist(self):
        _logger.debug('* * *  Checklist changed * * *')
        self._compute_progress()

        values = []
        for cb in self.checklist_item_ids:
            values.append(cb.id.origin)
        values = list(set(values))

        the_id = self.id.origin

        self.write({ 'checklist_item_ids': [(6, the_id, values)] })