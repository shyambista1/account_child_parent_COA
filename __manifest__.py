# -*- coding: utf-8 -*-
{
    'name': "Chart Of Accounts Child Parent Relationship",

    'summary': """
        This Module is use to Add Child Parent Relationship of accounts in the chart of accounts. """,

    'description': """
        Add Child Parent Relationship in the Chart of accounts by assigning parent account to the account.
    """,

    'author': 'Myself',
    'category': 'Accounting',
    'version': '17.0.1.0.0',

    'depends': ['account'],

    'data': [
        'data/data_account_type.xml',
        'views/account_account_views.xml',
    ],
    
    'auto_install': False,
    'installable': True,
    'application': False
}
