#-*- coding: utf-8 -*-

from odoo import models, fields, api

class compteur(models.Model):
    _name = "eaglefuel.compteur"
    _description = "compteur"
    # _rec_name = "ref"

    ref = fields.Char("Reference")
    numero = fields.Char("Numero")
    pistole_id = fields.Many2one("eaglefuel.pistole", "Pistole id")
    releveindex_id = fields.One2many("eaglefuel.releveindex", "compteur_id", string="Releve index")

    def name_get(self):
        result = []
        for compteur in self:
            name = str("[") + str(compteur.pistole_id.pompe_id.ref) +str("] ") + str(compteur.ref)
            result.append((compteur.id, name))
        return result


