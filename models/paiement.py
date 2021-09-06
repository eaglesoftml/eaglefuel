#-*- coding: utf-8 -*-

from odoo import models, fields, api

class paiement(models.Model):
    _name = 'eaglefuel.paiement'
    _description = 'Paiement'
    # _rec_name = "ref"

    ref = fields.Char("Paiement")
    type = fields.Selection(selection=[('a', 'Cash'),('b', 'Credit'),('c','Mobile')],required=True)
    montant = fields.Integer('Montant',required=True)
    servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste", string="services pompistes")
