# from odoo import http


# class Managateque(http.Controller):
#     @http.route('/managateque/managateque', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managateque/managateque/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managateque.listing', {
#             'root': '/managateque/managateque',
#             'objects': http.request.env['managateque.managateque'].search([]),
#         })

#     @http.route('/managateque/managateque/objects/<model("managateque.managateque"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managateque.object', {
#             'object': obj
#         })

