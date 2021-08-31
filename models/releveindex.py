#-*- coding: utf-8 -*-

from odoo import models, fields, api

class releveindex(models.Model):
    _name = "eaglefuel.releveindex"
    _description = "releveindex"

    ref = fields.Char("Reference")
    index = fields.Integer("Index depart", required=True)
    # index_arrive = fields.Integer("Index arrive", required=True)
    litrage_vendu = fields.Float("Litrage vendu", required=True)
    date_releve = fields.Datetime("Date du releve", required=True)
    compteur_id = fields.Many2one("eaglefuel.compteur", string="Compteur id")

    def name_get(self):
        result = []
        for releveindex in self:
            name = str("[") + str(releveindex.compteur_id.pompe_id.ilo_id.station_id.ref) +str("] ") + str(releveindex.ref)
            result.append((releveindex.id, name))
        return result