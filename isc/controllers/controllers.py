# from odoo import http


# class Isc(http.Controller):
#     @http.route('/isc/isc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/isc/isc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('isc.listing', {
#             'root': '/isc/isc',
#             'objects': http.request.env['isc.isc'].search([]),
#         })

#     @http.route('/isc/isc/objects/<model("isc.isc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('isc.object', {
#             'object': obj
#         })

