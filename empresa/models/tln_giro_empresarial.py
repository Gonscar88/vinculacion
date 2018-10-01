# -*- coding:utf-8 -*-

from odoo import fields, models

class tln_giro_empresarial(models.Model):
    _name = 'tln_giro_empresarial'

    name = fields.Char(
        string='Giro',
        required=True
    )
    codigo = fields.Char(
        string=u'Código',
    )
    
    