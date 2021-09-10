#-*- coding: utf-8 -*-
from odoo import models, fields, api

# class pompe(models.Model):
#     _name = "eaglefuel.pompe"
#     _description = "pompe"
#
#     pompe_number =fields.Integer("Numero de pompe", required=True)
#     nom = fields.Char("Reference de La pompe")
#     description = fields.Text()
#     #ilo_id = fields.Many2one("eaglefuel.ilo", string="Pompe Parent")
#     pistole_ids= fields.One2many("eaglefuel.pistole","pompe_id",  string= "Pistole")

class pompe(models.Model):
    _name = "eaglefuel.pompe"
    _description = "pompe"
    # _rec_name = "ref"

    pompe_number = fields.Integer("Numero de pompe", required=True)
    nom = fields.Char("nom de la pompe")
    description = fields.Text()

    ref = fields.Char("reference")
    litrage_essence = fields.Integer("Litrage essence", compute="qte_carb_vendu")
    litrage_gasoile = fields.Integer("Litrage Gasoile", compute="qte_carb_vendu")
    total_litres  = fields.Float("Litrage vendu", compute="qte_carb_vendu")
    # date_jour = fields.Date("Date", compute="date_service")
    # ilo_id = fields.Many2one("eaglefuel.ilo", "Ilo id")
    station_id = fields.Many2one("eaglefuel.station", string="station id")
    pistole_id = fields.One2many("eaglefuel.pistole", "pompe_id", string="pistole")
    servicepompiste_id = fields.One2many("eaglefuel.servicepompiste","pompe_id", string="services pompistes")

    def name_get(self):
        result = []
        for pompe in self:
            name = str("[") + str(pompe.station_id.ref) +str("] ") + str(pompe.ref)
            result.append((pompe.id, name))
        return result

    @api.depends('servicepompiste_id.litres_essence_vendu','servicepompiste_id.litres_gasoile_vendu','servicepompiste_id.litrage_vendu')
    def qte_carb_vendu(self):
        for record in self:
            litrage_essence = 0
            litrage_gasoile = 0
            total_litres = 0
            for line in record.servicepompiste_id:
                litrage_essence += line.litres_essence_vendu
                litrage_gasoile += line.litres_gasoile_vendu
                total_litres += line.litrage_vendu
            record.update({'litrage_essence': litrage_essence, 'litrage_gasoile': litrage_gasoile,'total_litres':total_litres})

