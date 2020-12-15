# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#        'security/ir.model.access.csv',
{
    'name' : 'Test',
    'version' : '14.0.1.1',
    'summary': 'Test adding new addon',
    'sequence': 15,
    'description': """
        Test adding new addon
        ====================
        Let say just a sand box area
    """,
    'category': 'Test',
    'author': 'Hisham Alwanni',
    'website': '/test/static/test.html',
    'images': [],
    'depends': [],
    'data': [

        'test.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
