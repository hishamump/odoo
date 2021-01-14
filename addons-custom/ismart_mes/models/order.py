# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields, _


class Order(models.Model):
    _inherit = 'mrp.production'

    process_id = fields.One2many('process', 'order_id', string="Processes")

    def create_process(self):
        return {
            'name': _('Process'),
            'domain': [],
            'view_type': 'form',
            'res_model': 'process',
            'view_id': False,
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            # TODO: This id order_id doesnt passed successfully, need more read
            'order_id': self._context.get('order_id', False)
        }
