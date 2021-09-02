#-*- coding: utf-8 -*-

from odoo import models, fields, api

class releveindex(models.Model):
    _name = "eaglefuel.releveindex"
    _description = "releveindex"

    ref = fields.Char("Reference")
    index = fields.Integer("Index", required=True)
    # index_arrive = fields.Integer("Index arrive", required=True)
    litrage = fields.Integer("Litrage", compute="litrage_vendu")
    date_releve = fields.Datetime("Date du releve", required=True)
    compteur_id = fields.Many2one("eaglefuel.compteur", string="Compteur id")

    def litrage_vendu(self):
        for line in self:
            line.litrage = line.index / 2

    def name_get(self):
        result = []
        for releveindex in self:
            name = str("[") + str(releveindex.compteur_id.pistole_id.pompe_id.ilo_id.station_id.ref) +str("] ") + str(releveindex.ref)
            result.append((releveindex.id, name))
        return result

