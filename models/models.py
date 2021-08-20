#-*- coding: utf-8 -*-

from odoo import models, fields, api


# class station(models.Model):
#  _name = 'station.station'
#  _description = 'Station'
#
#  name = fields.Char()
#  location = fields.Char()
#  #image = fields.binary("Image", help="Sectionner une image"),
#  description = fields.Text()
#  gps = fields.Char()
#  code = fields.Integer()
#  manager_id = fields.Many2one("res.users", "Responsable")
#  employee_ids=fields.One2many("hr.employee", "station_id", string="Pompistes")
# # tank_ids=fields.One2many("tank.tank", "station_id", string="Citernes")
#  product_ids=fields.One2many("product.product", "station_id", string="Produits")
#
# class tanktanks(models.Model):
#     _name = "cuve.cuve"
#     _description = "Tank"
#
#     station_id = fields.Many2one("eaglefuel.eaglefuel", string="Station")
#     container_ref = fields.Char("Ref citerne", required=True, index=True)
#     capacite_volume = fields.Char("Capacite")
#     longeur_regle = fields.Char("Taille max régle")
#     position = fields.Char("Position", required=True)
#     product_id = fields.Many2one("product.template", "Produit Stocké")
#     weight = fields.Float("Weight", required=True)
#     volume = fields.Float("Volume", required=True)
#
# class HrEmployee(models.Model):
#     _inherit = "hr.employee"
#     station_id = fields.Many2one("eaglefuel.eaglefuel", string="Station")
#
#
# class ProductFuel(models.Model):
#     _inherit = "product.product"
#     station_id = fields.Many2one("eaglefuel.eaglefuel", string="Station")
#


            