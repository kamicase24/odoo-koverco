# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /mnt/project/base_addons/koverko(models.Model):
#     _name = '/mnt/project/base_addons/koverko./mnt/project/base_addons/koverko'
#     _description = '/mnt/project/base_addons/koverko./mnt/project/base_addons/koverko'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
