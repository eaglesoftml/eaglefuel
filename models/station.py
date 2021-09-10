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

class station(models.Model):
    _name = 'eaglefuel.station'
    _description = 'Gas station'
    _rec_name = "ref"

    ref = fields.Char("reference")
    name = fields.Char("Nom de la station")
    adress = fields.Char("Adress de la station")
    description = fields.Text("description breve de station")
    image = fields.Binary(string="Image", help="Sectionner une image")
    gps = fields.Char()
    code = fields.Integer()

    # ilo_id = fields.One2many("eaglefuel.ilo", "station_id", string="ilo")
    pompe_id = fields.One2many("eaglefuel.pompe", "station_id", string="Pompes")
    cuve_id = fields.One2many("eaglefuel.cuve", "station_id", string="cuve")
    employe_id = fields.One2many("hr.employee", "station_id", string="employe")
    produit_id = fields.One2many("product.product", "station_id", string="Produit")


    # @api.depends('pompe_id.litrage_essence','pompe_id.litrage_gasoile','pompe_id.total_litres')
    # def qte_carb_vendu(self):
    #     for record in self:
    #         litrage_essence = 0
    #         litrage_gasoile = 0
    #         total_litres = 0
    #         for line in record.servicepompiste_id:
    #             litrage_essence += line.litres_essence_vendu
    #             litrage_gasoile += line.litres_gasoile_vendu
    #             total_litres += line.litrage_vendu
    #         record.update(
    #             {'litrage_essence': litrage_essence, 'litrage_gasoile': litrage_gasoile, 'total_litres': total_litres})
    #
    #


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    station_id = fields.Many2one("eaglefuel.station", string="Station")
    servicepompiste_qm_id = fields.Many2many("eaglefuel.servicepompiste", "QM_responsable")
    servicepompiste_pompiste_id = fields.One2many("eaglefuel.servicepompiste", "pompiste_id", "pompiste_responsable")
    jauge_id = fields.Many2many("eaglefuel.jauge", "jauges")
