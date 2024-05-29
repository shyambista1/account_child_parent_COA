# -*- coding: utf-8 -*-


from odoo import fields, models


class AccountAccountType(models.Model):
    _name = "account.account.type"

    type = fields.Selection(
        selection=[
            ('view', 'View'),
            ('asset', 'Asset'),
            ('liability', 'Liability'),
            ('income', 'Income'),
            ('expense', 'Expense'),
            ('consolidation', 'Consolidation'),
        ],
        string='Type',
        required=True,
        default='view',
        help="Select the type for this account type.",
    )
    include_initial_balance = fields.Boolean(string="Include Initial Balance")
    internal_group = fields.Selection(selection=[('view', 'View')])
