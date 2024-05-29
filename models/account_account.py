# -*- coding: utf-8 -*-


from odoo import fields, models

class AccountAccount(models.Model):
    _inherit = "account.account"
    parent_id = fields.Many2one('account.account', string="Parent Account")