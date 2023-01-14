# -*- coding: utf-8 -*-

from odoo import models, fields, api

class student(models.Model):
    _inherit = 'res.partner'
    name = fields.Char(string='Nombre Estudiante', requiered=True)
    lastname = fields.Char(string='Apellidos', requiered=True)
    genero = fields.Selection([('male', 'Masculino'),
                               ('female', 'Femenino'),
                               ('other', 'Other')],
                              string='Género', required=True, default='female',
                              track_visibility='onchange')
    telefono = fields.Char(string='Telefono')
    email = fields.Char(string='Correo')
    number = fields.Integer(string='Número')
    seccion = fields.Char(string='Sección')
    status = fields.Boolean(string='No activo')
    #courses_ids = fields.Many2one('pvas.courses', string='Cursos', requiered=True)
    #carreras_ids = fields.Many2one('pvas.carreras', string='Carreras', requiered=True)
    #family = fields.Char(string="Familia", related='carreras_ids.family')
    #grados_ids = fields.Many2one('pvas.grados', string='Grados', requiered=True)