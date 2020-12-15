# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields


class Factory(models.Model):
    _name = 'factory'
    _description = 'The shop floor'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    serial = fields.Char(string='Serial')
    address = fields.Char(string='address')
    notes = fields.Char(string='Notes')

