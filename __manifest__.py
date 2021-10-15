# -*- coding: utf-8 -*-
{
    'name': "eaglegasstation",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        The purpose of this module is to manage multi station gas compagny
    """,

    'author': "Eaglesoft SA",
    'website': "http://www.eaglesoftconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',    
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'stock', 'sale', 'account','product','mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/eaglefuel_view.xml',
        'views/station_view.xml',
        # 'views/ilo_view.xml',
        'views/pompe_view.xml',
        'views/pistole_view.xml',
        'views/compteur_view.xml',
        'views/cuve_view.xml',
        'views/servicepompiste_view.xml',
        'views/jauge_view.xml',
        # 'views/versement_view.xml',
        'views/releveindex_view.xml',
        # 'views/produit_view.xml',
        # 'views/detailventecarburant_view.xml',
        'views/paiement_view.xml',
        'views/rapportjournalier_view.xml',
        # 'views/website_templates.xml',
        # 'views/website_favicon.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'application': True,
}

