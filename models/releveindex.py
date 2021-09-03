#-*- coding: utf-8 -*-

from odoo import models, fields, api

class releveindex(models.Model):
    _name = "eaglefuel.releveindex"
    _description = "releveindex"

    ref = fields.Char("Reference")
    index_matin = fields.Integer("Index matin", required=True)
    index_soir = fields.Integer("Index soir", required=True)
    litrage = fields.Integer("Litrage", compute="litrage_vendu")
    carburant = fields.Many2one(related="compteur_id.pistole_id")
    date_releve = fields.Datetime("Date du releve", required=True)
    compteur_id = fields.Many2one("eaglefuel.compteur", string="Compteur id")
    servicepompiste_id = fields.Many2one("eaglesoft.servicepompiste", string="service pompiste id")


    def litrage_vendu(self):
        for line in self:
            line.litrage = line.index_soir - line.index_matin

    def name_get(self):
        result = []
        for releveindex in self:
            name = str("[") + str(releveindex.compteur_id.pistole_id.pompe_id.ilo_id.station_id.ref) +str("] ") + str(releveindex.ref)
            result.append((releveindex.id, name))
        return result

