#-*- coding: utf-8 -*-

from odoo import models, fields, api


# class station(models.Model):
#  _name = 'eaglefuel.station'
#  _description = 'Gas station'
#
#  name = fields.Char()
#  image = fields.Binary(string="Image", help="Sectionner une image"),
#  location = fields.Char()
#  description = fields.Text()
#  gps = fields.Char()
#  code = fields.Integer()

#  manager_id = fields.Many2one("res.users", "Responsable")
#  employee_ids=fields.One2many("hr.employee", "station_id", string="Pompistes")
#  cuve_ids=fields.One2many("eaglefuel.cuve", "station_id", string="Cuves")
#  product_ids=fields.One2many("product.product", "station_id", string="Produits")
#
#
# class HrEmployee(models.Model):
#     _inherit = "hr.employee"
#     station_id = fields.Many2one("eaglefuel.station", string="Station")
#
#
# class ProductFuel(models.Model):
#     _inherit = "product.product"
#     station_id = fields.Many2one("eaglefuel.station", string="Station")
#

class station(models.Model):
    _name = 'eaglefuel.station'
    _description = 'Gas station'

    name = fields.Char("Nom de la station")
    adress = fields.Char("Adress de la station")
    description = fields.Text("description breve de station")
    image = fields.Binary(string="Image", help="Sectionner une image")
    gps = fields.Char()
    code = fields.Integer()

    ilo_id = fields.One2many("eaglefuel.ilo", "station_id", string="ilo")

