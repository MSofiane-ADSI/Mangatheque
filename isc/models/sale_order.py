from odoo import models, fields, api
from . import sale_order

class SaleOrder(models.Model):

    _inherit='sale.order'

    premier_acompte = fields.Monetary(
        string='Acompte', 
        compute='_compute_premier_acompte', 
        store=True,
        currency_field='currency_id'  
    )

    @api.depends('amount_total')  
    def _compute_premier_acompte(self):
        for rec in self:
            rec.premier_acompte = 500 if rec.amount_total > 1000 else 0
