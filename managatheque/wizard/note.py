from odoo import models, fields, api

class NoteWizard(models.TransientModel):
    _name = 'managatheque.note.wizard'
    _description = 'Wizard pour donner une note'

    manga_id = fields.Many2one('managatheque.managatheque', string='Manga', required=True)
    
    note = fields.Integer(string='Note', required=True)

    def action_valider(self):
        self.ensure_one()
        self.manga_id.note = self.note
        return {'type': 'ir.actions.act_window_close'}