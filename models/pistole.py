#-*- coding: utf-8 -*-
from odoo import models, fields, api

class pistole(models.Model):
    _name = "eaglefuel.pistole"
    _description = "pistole"
    # _rec_name = "ref"

    ref = fields.Char("reference", default="New")
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
            name = str("[") + str(pistole.pompe_id.station_id.ref) +str("] ") + "/" + str(pistole.pompe_id.ref) + "/" + str(pistole.ref)
            result.append((pistole.id, name))
        return result

    @api.model
    def create(self, values):
        res = super(pistole, self).create(values)
        res.write({ref: f'{pompe_id}/{res.id}'})
        return res

    @api.model
    def create(self, values):
        values['ref'] = self.env['ir.sequence'].next_by_code('seq.pistole.ref') or _('New')
        return super(pistole, self).create(values)
