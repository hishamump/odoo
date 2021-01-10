# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields


class WorkstationData(models.Model):
    _name = 'workstation.data'
    _description = 'Data of workstation through the processes'

    workstation_id = fields.Many2one('workstation',
                                     ondelete='cascade', string="Workstation", required=True)
    process_id = fields.Many2one('process',
                                 ondelete='cascade', string="Process", required=True)
    record_datetime = fields.Char(string='Date')
    power_read = fields.Char(string='Notes')
    fuel_read = fields.Binary('Image')
    vibration_read = fields.Integer('Order')
    status = fields.Selection([
        ('off', 'Off'),
        ('working', 'Working'),
        ('idle', 'Idle'),
        ('broken', 'Broken'),
        ('disable', 'Disable')], required=True, default='off',
        help="The status of the workstation.")
