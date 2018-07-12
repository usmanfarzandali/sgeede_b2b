# -*- encoding: utf-8 -*-
{
	'name': 'SGEEDE Sale Order Cost',
	'version': '1.0',
	'category': 'Tools',
	'summary':"""Module to show cost price in sale order""",
	'description': """Module to show cost price in sale order""",
	'author': 'SGEEDE',
	'website': 'http://www.sgeede.com',
	'depends': ['sale'],
	'data': [
		'security/sgeede_sale_order_cost_security.xml',
		'views/sale_extend_view.xml',
	],
	'qweb': ['static/src/xml/*.xml'],
	'demo_xml': [],
	'installable': True,
	'active': False,
	'price': 9.99,
	'currency': 'EUR',
	'license': 'LGPL-3',
	'images': [
		'images/main_screenshot.png',
		'images/sgeede.png',
	],
}