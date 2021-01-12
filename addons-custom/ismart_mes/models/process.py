# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields, _, api


class Process(models.Model):
    _name = 'process'
    _description = 'Production Processes'

    process_sequence = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                                   index=True, default=lambda self: _('New'))
    name = fields.Char(string='Name')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    order_id = fields.Many2one('mrp.production',
                               ondelete='set null', string="Order", index=True)

    @api.model
    def create(self, values):
        if values.get('process_sequence', _('New')) == _('New'):
            values['process_sequence'] = self.env['ir.sequence'].next_by_code('ismart.mes.process.sequence') or _('New')
        result = super(Process, self).create(values)
        return result

    def start(self):
        print("Started")

    def stop(self):
        print("Started")
