# -*- coding: utf-8 -*-
from odoo import http


class koverko(http.Controller):
    @http.route('/koverko', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/koverkokoverkoobjects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/project/base_addons/koverko.listing', {
#             'root': '/koverko/mnt/project/base_addons/koverko',
#             'objects': http.request.env['/mnt/project/base_addons/koverko./mnt/project/base_addons/koverko'].search([]),
#         })

#     @http.route('/koverkokoverkoobjects/<model("/mnt/project/base_addons/koverko./mnt/project/base_addons/koverko"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/project/base_addons/koverko.object', {
#             'object': obj
#         })
