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
    ilo_id = fields.Many2one("eaglefuel.ilo", "Ilo id")
    pistole_id = fields.One2many("eaglefuel.pistole", "pompe_id", string="pistole")
    servicepompiste_id = fields.One2many("eaglefuel.servicepompiste","pompe_id", string="services pompistes")

    def name_get(self):
        result = []
        for pompe in self:
            name = str("[") + str(pompe.ilo_id.station_id.ref) +str("] ") + str(pompe.ref)
            result.append((pompe.id, name))
        return result
