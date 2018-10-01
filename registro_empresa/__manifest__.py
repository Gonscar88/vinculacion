# -*- coding: utf-8 -*-
{
    'name': "Talent - Registro Empresa",

    'summary': """Modulo para el registro de empresas""",

    'description': """
================================================================================

1.Registrar Usuario Empresa desde el sitio web.

================================================================================ 
    """,

    'author': "PCS",
    'website': "",
    'category': 'Test',
    'version': '0.1',
    'depends': [
        'base',
        'website',
        'website_form',
        'website_partner',
        'website_mail',
        'web_principal',
        'empresa',
        'hr'
    ],

    'data': [
        #'data/menu_opciones.xml',
        'views/registro_empresa_web.xml',
        'views/homepage_inherit.xml',
    ],
    'installable': True,
    'auto_install': False,
}