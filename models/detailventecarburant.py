#-*- coding: utf-8 -*-

from odoo import models, fields, api

class detailventecarburant(models.Model):
    _name = "eaglefuel.detailventecarburant"
    _description = "detail des ventes du carburant"

    nom_carb = fields.Selection(selection=[('a', 'Essence'),('b', 'Gasoile')])
    pu = fields.Integer("prix unitaire", compute="calcul_prix_unitaire")
    # montant = fields.Integer("Montant", compute="montant_carb")
    #produit_id = fields.Many2one("product.product",  string="carburant")
    servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste", string="service pompiste")

    def calcul_prix_unitaire(self):
        # prix_essence = 663
        # prix_gasoile = 593
        for line in self:
            if line.nom_carb == "a":
                line.pu = 663
            elif line.nom_carb == "b":
                line.pu = 593
            else:
                line.pu = 1