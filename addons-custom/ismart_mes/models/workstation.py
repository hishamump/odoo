# -*- coding: utf-8 -*-
# Created by Hisham.
import json

import requests

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
    image = fields.Image('Image', max_width=300, max_height=300)

    power_read = fields.Float(string='Power', digits=(12, 3), readonly=True)
    fuel_read = fields.Float(string='Fuel', digits=(12, 3), readonly=True)
    vibration_read = fields.Float(string='Vibration', digits=(12, 3), readonly=True)
    status = fields.Selection([
        ('off', 'Off'),
        ('working', 'Working'),
        ('idle', 'Idle'),
        ('broken', 'Broken'),
        ('disable', 'Disable')], required=True, default='off', readonly=True,
        help="The status of the workstation.")

    @api.model
    def create(self, values):
        if values.get('workstation_sequence', _('New')) == _('New'):
            values['workstation_sequence'] = self.env['ir.sequence'].next_by_code(
                'ismart.mes.workstation.sequence') or _('New')
        result = super(Workstation, self).create(values)
        return result

    def get_workstation_status(self):
        resp = requests.get('http://localhost:8012/machine/data.php')
        if resp.status_code == 200:
            print('GET SUCCESS !!!!')
            json_data = resp.json()
            obj = next(w for w in json_data if w["id"] == self.workstation_sequence)
            Workstation.json_print(obj)
            self.power_read = obj["power"]
            self.vibration_read = obj["vibration"]
            self.status = obj["status"]
            print(self.power_read)
            print(self.vibration_read)
            return json_data
        else:
            # This means something went wrong.
            print('GET ERROR: '.format(resp.status_code))

    @staticmethod
    def json_print(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
