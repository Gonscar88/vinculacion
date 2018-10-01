# -*- coding: utf-8 -*-
{
    'name': "Talent - Empresa",

    'summary': """
        Administrar empresas""",

    'description': """
        Registro y administración de empresas a la plataforma
    """,

    'author': "PCS",
    'website': "",

    'category': 'Extra Tools',
    'version': '0.1',

    'depends': [
        'base',
        'itm_material'
    ],

    'data': [
        'security/tln_groups.xml',
        'security/ir.model.access.csv',
        'views/tln_giro_empresarial.xml',
        'views/tln_res_company_inherit.xml',
        'views/tln_menu.xml',
    ],

    'installable': True,
    'auto_install': False,
}