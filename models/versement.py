#-*- coding: utf-8 -*-

from odoo import models, fields, api

class versement(models.Model):
    _name = "eaglefuel.versement"
    _description = "versement"

    ref = fields.Char("reference")
    montant_versement = fields.Integer("Montant du versement")
    heure_versement = fields.Float("Heure du versement", required=True)
    nbre_versement = fields.Integer("Nombre de versement")
    total_versement = fields.Integer("Total somme verse")
    servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste", string="service pompiste")
