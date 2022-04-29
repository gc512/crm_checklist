# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.crm.models.crm_lead import Lead

import logging
_logger = logging.getLogger(__name__)

class ChecklistItem(models.Model):
    _name = 'crm.lead.checklist.item'
    _description = 'Entry on a lead checklist'

    _sql_constraints = [
        ('uniq_name', 'unique(name)', "A item with this name exists already")
    ]

    name = fields.Char(required=True, translate=True)

class ChecklistEntry(models.Model):
    _name = 'crm.lead.checklist.entry'
    _description = 'Relation between Lead and Checklist Item'
    _rec_name = 'item_id'

    lead_id = fields.Many2one('crm.lead', string='Chance', ondelete='cascade')
    item_id = fields.Many2one('crm.lead.checklist.item', string='ToDo', ondelete='cascade')
    done = fields.Boolean('Done', default=True)

    _sql_constraints = [
        ('uniq_entry', 'unique(lead_id,item_id)', "This item is on checklist already")
    ]

class Checklist(models.Model):
    _inherit = 'crm.lead'

    def _compute_progress(self):
        for rec in self:
            progress = 0

            if rec.checklist:
                max_items = len(rec.checklist)
                if max_items > 0:
                    fin_items = 0
                    for item in rec.checklist:
                        if item.done:
                            fin_items += 1

                    progress = 100 * fin_items / max_items

            rec.progress = progress

    @api.onchange('checklist')
    def _onchange_checklist(self):
        self._compute_progress()

    @api.model
    def _get_checklist_default(self):
        _logger.debug('* * * * * DEFAULTS * * * * *')

        avail_items = self.env['crm.lead.checklist.item']
        avail_item_ids = avail_items.search([])

        entries = []
        for rec in avail_item_ids:
            entries.append({
                'lead_id': self.env.uid,
                'item_id': rec.id,
                'done': True,
            })

        return entries

    checklist = fields.One2many(
        'crm.lead.checklist.entry',
        'lead_id',
        string="Checklist",
        copy=True,
        default=_get_checklist_default,
    )
    progress = fields.Integer(compute='_compute_progress')
