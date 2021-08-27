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
    rec_name = "ref"

    ref = fields.Char("reference")
    nom = fields.Char("Nom Ilo", required=True)
    number = fields.Integer("Numero ilo")
    description = fields.Text()

    station_id = fields.Many2one("eaglefuel.station", string="station id")
    pompe_id = fields.One2many("eaglefuel.pompe", "ilo_id", string="pompe")

    