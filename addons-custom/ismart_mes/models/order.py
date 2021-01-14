# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields


class Order(models.Model):
    _inherit = 'mrp.production'
