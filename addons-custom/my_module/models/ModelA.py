# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModelA(models.Model):
    _name = 'model.a'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    student_dob = fields.Date(string="Date of Birth")
    marks = fields.Float(string="marks")
    image = fields.Binary(string='Photo')
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], string='Gender')
    address = fields.Text()