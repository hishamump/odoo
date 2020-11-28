# -*- coding: utf-8 -*-
# Created by Hisham to test adding new module.

from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Created by Hisham'

    patient_name = fields.Char(string='Name')
    patient_age = fields.Integer('Age')
    notes = fields.Char(string='Notes')
    image = fields.Binary('Image')
