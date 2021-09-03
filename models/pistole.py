#-*- coding: utf-8 -*-
from odoo import models, fields, api

class pistole(models.Model):
    _name = "eaglefuel.pistole"
    _description = "pistole"
    # _rec_name = "ref"

    ref = fields.Char("reference")
    #counter_index =fields.Integer("Index Compteur",  required=True)
    number = fields.Integer("Numero de Pistole")
    #date_releve = fields.Datetime("Date relevé", required=True)
    produit_servi= fields.Selection(selection=[('e', 'Essence'),('g', 'Gasoile')])
    description = fields.Text()
    pompe_id = fields.Many2one("eaglefuel.pompe", string="Pompe id")
    compteur_id = fields.Many2one("eaglefuel.compteur", "compteur id")


    def name_get(self):
        result = []
        for pistole in self:
            name = str("[") + str(pistole.pompe_id.ilo_id.station_id.ref) +str("] ") + "/" + str(pistole.pompe_id.ref) + "/" + str(pistole.ref)
            result.append((pistole.id, name))
        return result