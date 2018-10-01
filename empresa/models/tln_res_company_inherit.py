#-*-coding:utf-8 -*-

from odoo import models,fields
class ResCompany_inherit(models.Model):
    _inherit = 'res.company'
    
    contact = fields.Char(
        string='Contacto',
    )
    giro_empresarial = fields.Many2one(
        string=u'Giro Empresarial',
        comodel_name='tln_giro_empresarial',
        ondelete='set null',
    )