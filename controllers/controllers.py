# -*- coding: utf-8 -*-
# from odoo import http


# class Registrodigital(http.Controller):
#     @http.route('/registrodigital/registrodigital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registrodigital/registrodigital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('registrodigital.listing', {
#             'root': '/registrodigital/registrodigital',
#             'objects': http.request.env['registrodigital.registrodigital'].search([]),
#         })

#     @http.route('/registrodigital/registrodigital/objects/<model("registrodigital.registrodigital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registrodigital.object', {
#             'object': obj
#         })
