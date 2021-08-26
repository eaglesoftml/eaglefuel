#-*- coding: utf-8 -*-

from odoo import models, fields, api

class jauge(models.Model):
    _name = 'eaglefuel.jauge'
    _description = "jauge"

    ref = fields.Char("reference")
    mesure_regle = fields.Float("jauge", required=True)
    date_jauge = fields.Datetime("Date du jauge", required=True)
    litrage_jauge = fields.Integer("Litrage jauge")
    cuve_id = fields.Many2one("eaglefuel.cuve", string="cuve")
    employe_id= fields.Many2many("hr.employee", string="QM responsable")