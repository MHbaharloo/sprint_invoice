    # -*- coding: utf-8 -*-
from openerp import http

# class SprintInvoice(http.Controller):
#     @http.route('/sprint_invoice/sprint_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sprint_invoice/sprint_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sprint_invoice.listing', {
#             'root': '/sprint_invoice/sprint_invoice',
#             'objects': http.request.env['sprint_invoice.sprint_invoice'].search([]),
#         })

#     @http.route('/sprint_invoice/sprint_invoice/objects/<model("sprint_invoice.sprint_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sprint_invoice.object', {
#             'object': obj
#         })