# -*- coding: utf-8 -*-
# Created by Hisham to test adding new module.

from odoo import models, fields


class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Created by Hisham'

    test_name = fields.Char('Test Name')
    image = fields.Binary('Image')
    just_number = fields.Integer('Num')
