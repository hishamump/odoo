# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'iSmart MES',
    'version' : '14.0.1.1',
    'summary': 'Module for managing a workstation',
    'sequence': -1,
    'description': """
        iSmart MES
        ====================
        Manufacturing Execution System
    """,
    'category': 'Manufacturing',
    'author': 'Hisham Alwanni',
    'website': '/ismart_mes/static/info.html',
    'images': [],
    'depends': ['mrp'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/dashboard.xml',
        'views/order.xml',
        'views/process.xml',
        'views/workstation.xml',
        'views/report.xml',
        # 'views/factory.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
