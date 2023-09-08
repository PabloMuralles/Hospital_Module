# -*- coding: utf-8 -*-
# from odoo import http


# class OmCustomPdf(http.Controller):
#     @http.route('/om_custom_pdf/om_custom_pdf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_custom_pdf/om_custom_pdf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_custom_pdf.listing', {
#             'root': '/om_custom_pdf/om_custom_pdf',
#             'objects': http.request.env['om_custom_pdf.om_custom_pdf'].search([]),
#         })

#     @http.route('/om_custom_pdf/om_custom_pdf/objects/<model("om_custom_pdf.om_custom_pdf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_custom_pdf.object', {
#             'object': obj
#         })
