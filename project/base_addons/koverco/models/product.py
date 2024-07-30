# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)



class ProductQrResult(models.Model):

    _name = 'product.qr.result'
    _description = 'QR resultado para productos'

    name = fields.Char(string='Batch Num.')
    sku = fields.Char(string='Sku')
    lot_number = fields.Char(string='Lot Num.')
    qty = fields.Float(string='Qty.')
    date = fields.Char(string='QR Date')


    def process_qr_data(self):
        for product_qr_result_id in self:
            log.info(product_qr_result_id.name)
            log.info("Hace cosas!!!")

            # Search product
            product_id = self.env['product.product'].search([('default_code', '=', f'MIAMI:KSE-{product_qr_result_id.sku}')])
            if product_id:
                log.info(product_id)
                log.info(f'Product encontrado {product_id}')

                # Create lot record
                lot_number = product_qr_result_id.lot_number
                if lot_number:
                    lot_id = self.env['stock.lot'].search([('name', '=', lot_number)])
                    if not lot_id:
                        lot_data = {
                            'name': lot_number,
                            'product_qty': product_qr_result_id.qty,
                            'ref': lot_number,
                            'product_id': product_id.id,
                            'company_id': product_qr_result_id.env.user.company_id.id
                        }
                        lot_id = self.env['stock.lot'].create(lot_data)
                        log.info(f'Lote creado {lot_id}')
                    else:
                        log.info(f'Lote ya existe {lot_id}')


                    # Create stock quant
                    quant_data = {
                        'product_id': product_id.id,
                        'lot_id': lot_id.id,
                        'location_id': self.env.ref('stock.stock_location_stock').id,
                        'user_id': product_qr_result_id.env.user.id,
                    }
                    stock_quant_id = self.env['stock.quant'].create(quant_data)
                    log.info(f'Stock Quant creado {stock_quant_id}')
                    stock_quant_id.update({
                        'inventory_quantity': product_qr_result_id.qty,
                        # 'inventory_diff_quantity': product_qr_result_id.qty,
                    })
                    stock_quant_id._compute_inventory_diff_quantity()
                    stock_quant_id.action_apply_inventory()

                    log.info(f'Stock Quant actualizado')
                    adjustment_wizard = self.env['stock.inventory.adjustment.name'].create({
                        'inventory_adjustment_name': 'Ajuste de inventario por QR',
                    })
                    adjustment_wizard.action_apply()
                    log.info(f'accion aplicada {adjustment_wizard}')

            else:
                log.error(f'Product no encontrado {product_id}')