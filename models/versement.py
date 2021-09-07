#-*- coding: utf-8 -*-

from odoo import models, fields, api

class versement(models.Model):
    _name = "eaglefuel.versement"
    _description = "versement"
    # _rec_name = "ref"

    ref = fields.Char("reference")
    montant_versement = fields.Float("Montant du versement")
    # heure_versement = fields.Float("Heure du versement", required=True)
    # nbre_versement = fields.Integer("Nombre de versement")
    total_versement = fields.Float("Total somme verse")
    servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste", string="service pompiste")

    def name_get(self):
        result = []
        for versement in self:
            name = str("[") + str(versement.servicepompiste_id.pompe_id.ilo_id.station_id.ref) +str("] ") +str("/ ") + str(versement.servicepompiste_id.ref) + str(versement.ref)
            result.append((versement.id, name))
        return result
