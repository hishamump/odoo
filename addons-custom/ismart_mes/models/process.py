# -*- coding: utf-8 -*-
# Created by Hisham.

from odoo import models, fields


class Process(models.Model):
    _name = 'process'
    _description = 'Production Processes'

    name = fields.Char(string='Name')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    order_id = fields.Many2one('mrp.production',
                               ondelete='set null', string="Order", index=True)

    def start(self):
        print("Started")

    def stop(self):
        print("Started")
