# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospial Management',
    'version' : '14.0.1.1',
    'summary': 'Module for managing a hospital',
    'sequence': 2,
    'description': """
        Test adding new addon
        ====================
        Let say just a sand box area
    """,
    'category': 'Extra Tools',
    'author': 'Hisham Alwanni',
    'website': '/test/static/test.html',
    'images': [],
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'patient.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
