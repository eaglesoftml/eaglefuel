#-*- coding: utf-8 -*-
from odoo import models, fields, api

class ilo(models.Model):
    _name = "eaglefuel.ilo"
    _description = "ilo"
    
    nom  =fields.Char("Reference Ilo", required=True)
    number = fields.Integer("Réference Ilo")
    description = fields.Text()
    #pompe_ids = fields.One2many("eaglefuel.pompe", string="Pompe Parent")
    