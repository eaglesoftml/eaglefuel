#-*- coding: utf-8 -*-

from odoo import models, fields, api

class compteur(models.Model):
    _name = "eaglefuel.compteur"
    _description = "compteur"
    # _rec_name = "ref"

    ref = fields.Char("reference")
    index = fields.Integer("Index Compteur",  required=True)
    previous_index = fields.Integer()
    date_releve = fields.Datetime("Date du releve")
    pompe_id = fields.Many2one("eaglefuel.pompe", "pompe id")

    def name_get(self):
        result = []
        for compteur in self:
            name = str("[") + str(compteur.pompe_id.ref) +str("] ") + str(compteur.ref)
            result.append((compteur.id, name))
        return result


