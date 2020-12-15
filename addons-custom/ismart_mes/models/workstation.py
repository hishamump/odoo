# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields


class Workstation(models.Model):
    _name = 'workstation'
    _description = 'Basic production unit'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    serial = fields.Char(string='Serial')
    location = fields.Char(string='Location')
    notes = fields.Char(string='Notes')
    image = fields.Binary('Image')
    production_order = fields.Integer('Order')
