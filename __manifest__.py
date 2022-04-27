# -*- coding: utf-8 -*-
{
    'name': "CRM Lead Checklist Plugin",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "GHOSTCODERS GmbH",
    'website': "http://www.ghostcoders.com",

    'category': 'Sales/CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'crm'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    # only loaded in demonstration mode
    #'demo': [
        #'demo/demo.xml',
    #],

    #'installable': True,
    #'application': False,
    'auto_install': True,

    'license': 'LGPL-3',
}
