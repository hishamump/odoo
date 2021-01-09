# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields


class Order(models.Model):
    _inherit = 'mrp.production'
    _name = 'order'
    _description = 'Production Orders'

    name = fields.Char("Process", required=True)
