from odoo import fields, models, api


class Manga(models.Model):
    _name = 'managatheque.managatheque'
    #_name = "mangatheque.manga"
    _description = "Manga"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Titre", required=True, tracking=True)
    annee_parution = fields.Integer("Année de parution")
    auteur = fields.Many2one("res.partner", string="Auteur")
    #image_couverture = fields.Binary("Couverture")

    image_couverture = fields.Image(string='Photo')          # ← champ image
    note = fields.Integer(string='Note', tracking=True)                                    # stocke la note
    note_texte = fields.Char(string='Score', compute='_compute_note_texte', store=True)  # affichage

    @api.depends('note')
    def _compute_note_texte(self):
        for rec in self:
            rec.note_texte = f"Note : {rec.note}/20" if rec.note else ""
