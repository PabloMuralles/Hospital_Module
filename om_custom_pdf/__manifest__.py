# -*- coding: utf-8 -*-
{
    'name': "om_custom_pdf",

    'summary': "custom the pdf of odoo",

    'description': "Custom de pdf of sales, invoice and wherahouse",

    'author': "Pablo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/modify_existing_layout.xml',
        'report/custom_template.xml',
        'report/custom_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
