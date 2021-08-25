#-*- coding: utf-8 -*-

from odoo import models, fields, api

class compteur(models.Model):
    _name = "eaglefuel.compteur"
    _description = "compteur"

    ref = fields.Char()
    index = fields.Integer("Index Compteur",  required=True)
    previous_index = fields.Integer()
    pompe_id = fields.Many2one("eaglefuel.pompe", "pompe parent")
    date_releve = fields.Datetime("Date du releve")


