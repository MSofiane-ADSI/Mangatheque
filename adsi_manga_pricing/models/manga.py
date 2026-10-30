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
    ##########lab SIMI
    ##########lab SIMI
    ##########lab SIMI
    ##########lab SIMI
    ##########lab SIMI
    ##########lab SIMI
    ##########lab SIMI

    similar_manga_ids = fields.Many2many(
        comodel_name="managatheque.managatheque",
        relation="adsi_manga_pricing_similar_rel",
        column1="manga_id",
        column2="similar_manga_id",
        string="Similar Manga",
        help="Manga related to this manga.",
    )

    similar_manga_count = fields.Integer(
        string="Similar Manga Count",
        compute="_compute_similar_manga_count",
    )

    @api.depends("similar_manga_ids")
    def _compute_similar_manga_count(self):
        for manga in self:
            manga.similar_manga_count = len(manga.similar_manga_ids)

    def action_view_similar_manga(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "name": _("Similar Manga"),
            "res_model": "managatheque.managatheque",
            "view_mode": "list,form",
            "domain": [("id", "in", self.similar_manga_ids.ids)],
            "context": {
                "default_similar_manga_ids": [(6, 0, [self.id])],
            },
        }

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