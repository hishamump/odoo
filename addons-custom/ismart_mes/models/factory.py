# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields, api, _


class Factory(models.Model):
    _name = 'factory'
    _description = 'The shop floor'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    serial = fields.Char(string='Serial')
    address = fields.Char(string='Address')
    notes = fields.Char(string='Notes')
    factory_sequence = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                                   index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('factory_sequence', _('New')) == _('New'):
            vals['factory_sequence'] = self.env['ir.sequence'].next_by_code('ismart.mes.factory.sequence') or _('New')
        result = super(Factory, self).create(vals)
        return result
