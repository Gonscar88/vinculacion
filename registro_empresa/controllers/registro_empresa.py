# -*- coding: utf-8 -*-
import json
import base64
from odoo import http
from odoo.http import request


class RegistroEmpresa(http.Controller):

    @http.route('/page/registro_empresa.tln_registro_empresa', type='http', auth='public', website=True)
    def render_registro_empresa(self):
        return http.request.render('registro_empresa.tln_registro_empresa', {})

    @http.route('/page/registro_empresa.registro_empresa_success', type='http', auth='public', website=True)
    def render_registro_empresa_success(self):
        return http.request.render('registro_empresa.registro_empresa_success', {})

    @http.route('/website/create_empresa', type='http', methods=['POST', 'GET'], auth='public', website=True)
    def create_empresa_user(self, **kw):
        name = kw.get('name')
        email = kw.get('email')
        contacto = kw.get('contacto')
        telefono = kw.get('telefono')
        
        if request.env["res.users"].sudo().search([("login", "=", email)]):
            error = "Otro usuario ya está registrado usando esta dirección de correo electrónico"
            return http.request.render('registro_empresa.tln_registro_empresa', {'error':error})
        else:
            # =================crear registro res.company para multicompany
            company_record = http.request.env['res.company'].sudo().create({'name':name})
            # =================crear usuario
            user_data = {
                'name': name,
                'login': email,
                'company_ids':[(4, company_record.id)] ,
                'company_id':company_record.id,
            }            
            user_record = http.request.env['res.users'].sudo().create(user_data)
            user_accion_inicial = http.request.env.ref('empresa.tln_res_company_inherit_action')
            user_record.sudo().write({'action_id':user_accion_inicial.id})
            # =================asignar usuario permisos de usuario de portal  y responsable de reclutamiento                     
            user_group = http.request.env.ref('base.group_portal')
            user_group.sudo().write({'users': [(4, user_record.id)]})
            recruitment_group = http.request.env.ref('hr_recruitment.group_hr_recruitment_manager')
            recruitment_group.sudo().write({'users': [(4, user_record.id)]})
            # =================asignar usuario grupo de empresa
            user_group_empresa = http.request.env.ref('empresa.tln_empresa_group')
            user_group_empresa.sudo().write({'users': [(4, user_record.id)]})
            # =================asignar usuario un registro tipo res.partner
            user_partner = request.env["res.partner"].sudo().search([("id", "=", user_record.partner_id.id)])
            user_partner.sudo().write({'email':email})
            # =================enviar correo de confirmacion
            mail = user_record.sudo().with_context(create_user=True).action_reset_password()
            # =================crear registro tln_empresa y asignar el usuario
            empresa_datos ={
                'name':name,
                'contacto_nombre':contacto,
                'telefono':telefono,
                'email':email,
                'user_id': user_record.id,
            }
            #empresa_record = http.request.env['tln_empresa'].sudo().create(empresa_datos)
            
        return http.request.redirect('/page/registro_empresa.registro_empresa_success')
