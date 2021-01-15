# -*- coding: utf-8 -*-
# Created by Hisham.
import json

import requests
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
    status = fields.Selection([
        ('inprogress', 'In Progress'),
        ('pause', 'Pause'),
        ('stop', 'Stop'),
        ('off', 'Off')], default='off',
        help="The status of the process.")

    @api.model
    def create(self, values):
        if values.get('process_sequence', _('New')) == _('New'):
            values['process_sequence'] = self.env['ir.sequence'].next_by_code('ismart.mes.process.sequence') or _('New')
        result = super(Process, self).create(values)
        return result

    def start_process(self):
        resp = requests.get('http://localhost:8012/machine/start.php')
        if resp.status_code == 200:
            json_data = resp.json()
            Process.json_print(json_data)
            self.status = 'inprogress'
            print("Started")
        else:
            print("Error")

    def stop_process(self):
        resp = requests.get('http://localhost:8012/machine/stop.php')
        if resp.status_code == 200:
            json_data = resp.json()
            Process.json_print(json_data)
            self.status = 'stop'
            print("Stopped")
        else:
            print("Error")

    @staticmethod
    def json_print(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
