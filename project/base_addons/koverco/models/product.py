# -*- coding: utf-8 -*-

from odoo import models, fields, api



class ProductQrResult(models.Model):

    _name = 'product.qr.result'
    _description = 'QR resultado para productos'

    name = fields.Char(string='Batch Num.')
    sku = fields.Char(string='Sku')
    lot_number = fields.Char(string='Lot Num.')
    qty = fields.Float(string='Qty.')
    date = fields.Char(string='QR Date')


