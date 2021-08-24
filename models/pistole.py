#-*- coding: utf-8 -*-
from odoo import models, fields, api

class pistole(models.Model):
    _name = "eaglefuel.pistole"
    _description = "pistole"

    #counter_index =fields.Integer("Index Compteur",  required=True)
    number = fields.Integer("Réference de Pistole")
    #date_releve = fields.Datetime("Date relevé", required=True)
    produit_servi_id= fields.Many2one("product.product", "Produit Servi")
    description = fields.Text()
    pompe_id = fields.Many2one("eaglefuel.pompe", string="Pompe Parent")

    