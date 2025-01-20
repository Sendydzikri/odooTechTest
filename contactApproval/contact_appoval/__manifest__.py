# -*- coding: utf-8 -*-
{
    'name': "contactApproval",

    'summary': "Module custom contact approval",

    'description': """
Long description of module's purpose
    """,

    'author': "Sendy Dzikri Ferdiansyah",
    'website': "https://jukesolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'module_type': 'official',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase'],

    # always loaded
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/res_partner.xml",
        "views/filter_customer_vendor.xml",
        "views/views.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}

