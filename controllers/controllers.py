# -*- coding: utf-8 -*-
# from odoo import http


# class Eaglefuel(http.Controller):
#     @http.route('/eaglefuel/eaglefuel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eaglefuel/eaglefuel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eaglefuel.listing', {
#             'root': '/eaglefuel/eaglefuel',
#             'objects': http.request.env['eaglefuel.eaglefuel'].search([]),
#         })

#     @http.route('/eaglefuel/eaglefuel/objects/<model("eaglefuel.eaglefuel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eaglefuel.object', {
#             'object': obj
#         })
