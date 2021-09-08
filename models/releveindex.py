#-*- coding: utf-8 -*-

from odoo import models, fields, api

class releveindex(models.Model):
    _name = "eaglefuel.releveindex"
    _description = "releveindex"

    ref = fields.Char("Reference")
    index_matin = fields.Integer("Index depart", required=True)
    index_soir = fields.Integer("Index arrive", required=True)
    litrage = fields.Float("Litrage", compute="litrage_vendu")
    carburant = fields.Char(compute="nom_carb")
    date_releve = fields.Datetime("Date du releve", required=True)
    compteur_id = fields.Many2one("eaglefuel.compteur", string="Compteur id")
    servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste", string="service pompiste id")


    def litrage_vendu(self):
        for line in self:
            line.litrage = line.index_soir - line.index_matin

    def name_get(self):
        result = []
        for releveindex in self:
            name = str("[") + str(releveindex.compteur_id.pistole_id.pompe_id.ilo_id.station_id.ref) +str("] ") + str(releveindex.ref)
            result.append((releveindex.id, name))
        return result

    def nom_carb(self):
        for line in self:
            if line.compteur_id.pistole_id.produit_servi == "e":
                line.carburant = "Essence"
            else:
                line.carburant = "Gasoile"