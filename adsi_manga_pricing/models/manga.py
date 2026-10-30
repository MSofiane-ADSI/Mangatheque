from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare


class Manga(models.Model):
    _inherit = "managatheque.managatheque"

    purchase_cost = fields.Float(
        string="Purchase Cost",
        required=True,
        default=0.0,
        digits=(16, 2),
        help="Purchase cost of the manga.",
    )

    sale_price = fields.Float(
        string="Sale Price",
        required=True,
        default=0.0,
        digits=(16, 2),
        help="Sale price of the manga.",
    )

    margin = fields.Float(
        string="Margin",
        compute="_compute_margin",
        store=True,
        digits=(16, 2),
        help="Difference between the sale price and the purchase cost.",
    )

    @api.depends("purchase_cost", "sale_price")
    def _compute_margin(self):
        for manga in self:
            manga.margin = manga.sale_price - manga.purchase_cost

    @api.constrains("purchase_cost", "sale_price")
    def _check_pricing_rules(self):
        for manga in self:
            if manga.purchase_cost < 0.0:
                raise ValidationError(
                    _("The purchase cost must be greater than or equal to zero.")
                )

            if manga.sale_price < 0.0:
                raise ValidationError(
                    _("The sale price must be greater than or equal to zero.")
                )

            minimum_sale_price = manga.purchase_cost * 1.25

            if float_compare(
                manga.sale_price,
                minimum_sale_price,
                precision_digits=2,
            ) < 0:
            #if manga.sale_price < minimum_sale_price:
                raise ValidationError(
                    _(
                        "The sale price cannot be lower than 25% "
                        "of the purchase cost."
                    )
                )