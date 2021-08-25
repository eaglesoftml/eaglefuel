#-*- coding: utf-8 -*-

from odoo import models, fields, api

class jauge(models.Model):
    _name = 'eaglefuel.jauge'
    _description = "jauge"

    mesure_regle = fields.Float("jauge", required=True)
    date_jauge = fields.Datetime("Date du jaugage", required=True)
    cuve_id = fields.Many2one("eaglefuel.cuve", string="cuve")
    #employe_id= fields.One2many("hr.employee", "station_id", string="employe")