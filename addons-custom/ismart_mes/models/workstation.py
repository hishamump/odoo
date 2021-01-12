# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields, api, _


class Workstation(models.Model):
    _name = 'workstation'
    _description = 'Basic production unit'
    _rec_name = 'name'

    workstation_sequence = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                                   index=True, default=lambda self: _('New'))
    name = fields.Char(string='Name')
    location = fields.Char(string='Location')
    notes = fields.Char(string='Notes')
    image = fields.Binary('Image')

    @api.model
    def create(self, values):
        if values.get('workstation_sequence', _('New')) == _('New'):
            values['workstation_sequence'] = self.env['ir.sequence'].next_by_code('ismart.mes.workstation.sequence') or _('New')
        result = super(Workstation, self).create(values)
        return result