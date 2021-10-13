#-*- coding: utf-8 -*-

from odoo import models, fields, api

class compteur(models.Model):
    _name = "eaglefuel.compteur"
    _description = "compteur"
    # _rec_name = "ref"

    ref = fields.Char("Reference")
    numero = fields.Char("Numero")
    nom = fields.Char("Nom")
    pistole_id = fields.Many2one("eaglefuel.pistole", "Pistole id")
    releveindex_id = fields.One2many("eaglefuel.releveindex", "compteur_id", string="Releve index")

    def name_get(self):
        result = []
        for compteur in self:
            name = str("[") + str(compteur.pistole_id.pompe_id.nom) +str("] ") + str(compteur.nom)
            result.append((compteur.id, name))
        return result

    @api.model
    def create(self, values):
        res = super(compteur, self).create(values)
        res.write({ref: f'{pistole_id}/{res.id}'})
        return res

    @api.model
    def create(self, values):
        values['ref'] = self.env['ir.sequence'].next_by_code('seq.compteur.ref') or _('New')
        return super(compteur, self).create(values)


