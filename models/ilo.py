#-*- coding: utf-8 -*-
from odoo import models, fields, api

# class ilo(models.Model):
#     _name = "eaglefuel.ilo"
#     _description = "ilo"
#
#     nom  =fields.Char("Reference Ilo", required=True)
#     number = fields.Integer("Réference Ilo")
#     description = fields.Text()

    ##pompe_ids = fields.One2many("eaglefuel.pompe", string="Pompe Parent")

class ilo(models.Model):
    _name ="eaglefuel.ilo"
    _description = "ilo"

    nom = fields.Char("Nom Ilo", required=True)
    number = fields.Integer("Reference Ilo")
    description = fields.Text()

    station_id = fields.Many2one("eaglefuel.station", string="station parent")
    pompe_id = fields.One2many("eaglefuel.pompe", "ilo_id", string="pompe")
    servicepompiste_id = fields.One2many("eaglefuel.servicepompiste","ilo_id", string="services pompistes")

    