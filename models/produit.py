#-*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductFuel(models.Model):
    _inherit = "product.product"
    station_id = fields.Many2one("eaglefuel.station", string="Station")