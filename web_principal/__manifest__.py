# -*- coding: utf-8 -*-
{
    'name': "Talent - Vista principal",

    'summary': """Modulo para Heredar y editar la página principal""",

    'description': """
================================================================================

1. Heredar web de odoo
2. Modificar y adaptar a una vista propia

================================================================================ 
    """,

    'author': "pcs",
    'website': "",
    'category': 'Website',
    'version': '0.1',
    'depends': [
        'base',
        'website',
        'website_form',
        'website_partner',
        'website_mail'
    ],

    'data': [
        'views/navbar.xml',
        'views/homepage.xml',

        
    ],
    'installable': True,
    'auto_install': False,
}