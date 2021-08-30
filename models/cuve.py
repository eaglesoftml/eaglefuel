#-*- coding: utf-8 -*-

from odoo import models, fields, api

# class cuve(models.Model):
#     _name = "eaglefuel.cuve"
#     _description = "cuve"
#
#     station_id = fields.Many2one("eaglefuel.station", string="Station")
#     container_ref = fields.Char("Ref citerne", required=True, index=True)
#     capacite_volume = fields.Char("Capacite")
#     longeur_regle = fields.Char("Taille max régle")
#     ratioRV = fields.Float("Ratio Régle/Volume", required=True)
#     position = fields.Char("Position", required=True)
#     product_id = fields.Many2one("product.template", "Produit Stocké")
#     weight = fields.Float("Weight", required=True)
#     volume = fields.Float("Volume", required=True)



class cuve(models.Model):
    _name = 'eaglefuel.cuve'
    _description = 'Cuve'
    _rec_name = "ref"

    ref = fields.Char("reference")
    station_id = fields.Many2one("eaglefuel.station", string="station parent")
    longeur_regle = fields.Char("Taille max régle")
    diametre = fields.Float("Longueur", required=True)
    hauteur = fields.Float("Hauteur", required=True)
    volume = fields.Float("Volume") #pi*rcarre*h
    jauge_id = fields.One2many("eaglefuel.jauge", "cuve_id", string="jauge")

