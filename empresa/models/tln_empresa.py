# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Empresa(models.Model):
    _name = 'tln_empresa'

    name = fields.Char(
        string="Nombre",
        required='True'
    )    
    giro_empresarial = fields.Many2one(
        string=u'Giro Empresarial',
        comodel_name='tln_giro_empresarial',
        ondelete='set null',
    )
    
    image = fields.Binary(
        string=u'Foto',
    )

    contacto_nombre = fields.Char(
        string='Nombre de contacto'
    )

    fecha_actual = fields.Date(
        default=fields.Date.today
    )

    email = fields.Char(
        string='Email'
    )
    telefono = fields.Char(
        string='Teléfono'
    )
    celular = fields.Char(
        string='Celular'
    )

    calle = fields.Char(
        string='Calle',
    )

    colonia = fields.Char(
        string='Colonia',
    )
    municipio = fields.Char(
        string='Municipio',
    )
    country_id = fields.Many2one(
        'res.country',
        string='País',
    )
    state_id = fields.Many2one(
        'res.country.state',
        string='Estado'
    )
    cp = fields.Char(
        string=u'C.P.',
    )

    maps_latitud = fields.Float(
        string="Latitud: ",
        default='00.00000',
        digits=(16, 6)
    )
    maps_longitud = fields.Float(
        string="Longitud: ",
        default='00.00000',
        digits=(16, 6)
    )
    user_id = fields.Many2one(
        'res.users',
        string='Usuario',
    )
