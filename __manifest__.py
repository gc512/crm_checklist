# -*- coding: utf-8 -*-
{
    'name': "CRM Lead Checklist Plugin",

    'summary': """
        Use checklists to track progress in lead generation.""",

    'description': """
        The plugin adds a checklist to lead.
        Available checklist items can be configured by sales administrators.""",

    'author': "GHOSTCODERS GmbH",
    'website': "http://www.ghostcoders.com",

    'category': 'Sales/CRM',
    'version': '0.1',

    'depends': [
        'crm'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    #'installable': True,
    #'application': False,
    'auto_install': True,

    'license': 'LGPL-3',
}
