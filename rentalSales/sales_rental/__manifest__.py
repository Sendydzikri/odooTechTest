# -*- coding: utf-8 -*-
{
    'name': "Sales Rental",

    'summary': "Module custom Sales Rental",

    'description': """ Sales Rental
    """,

    'author': "Sendy Dzikri Ferdiansyah",
    'website': "https://jukesolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # only loaded in demonstration mode
    'data': [
        'views/menu.xml',
        'demo/demo.xml',
        'views/product_template_view.xml',
        'views/product_template_kanban_view.xml',
        'views/sale_order_form_view.xml',
        'views/sale_order_form_view_2.xml',
        'views/rental_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}

