#-*- coding: utf-8 -*-

from odoo import models, fields, api

class paiement(models.Model):
    _name = 'eaglefuel.paiement'
    _description = 'Paiement'
    # _rec_name = "ref"

    ref = fields.Char("Reference", default="New")
    nom = fields.Char("Nom")
    date = fields.Datetime("Date")
    description = fields.Char("Description")
    type = fields.Selection(selection=[('a', 'Cash'),('b', 'Credit'),('c','Mobile')],required=True)
    montant = fields.Float('Montant',required=True)
    servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste", string="services pompistes")


    def name_get(self):
        result = []
        for paiement in self:
            name = str("[") + str(paiement.servicepompiste_id.station_id.name) +str("] ") + "/" + str(paiement.servicepompiste_id.date) + "/" + str(paiement.servicepompiste_id.nom) + "/" + str(paiement.nom)
            result.append((paiement.id, name))
        return result

    @api.model
    def create(self, values):
        res = super(paiement, self).create(values)
        res.write({ref: f'{servicepompiste_id}/{res.id}'})
        return res

    @api.model
    def create(self, values):
        values['ref'] = self.env['ir.sequence'].next_by_code('seq.paiement.ref') or _('New')
        return super(paiement, self).create(values)
