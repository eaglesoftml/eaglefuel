#-*- coding: utf-8 -*-

from odoo import models, fields, api

# class cuve(models.Model):
#     _name = "eaglefuel.cuve"
#     _description = "cuve"
#
#     station_id = fields.Many2one("eaglefuel.station", string="Station")
#     container_ref = fields.Char("Ref citerne", required=True, index=True)
#     capacite_volume = fields.Char("Capacite")
#     longeur_regle = fields.Char("Taille max régle")
#     ratioRV = fields.Float("Ratio Régle/Volume", required=True)
#     position = fields.Char("Position", required=True)
#     product_id = fields.Many2one("product.template", "Produit Stocké")
#     weight = fields.Float("Weight", required=True)
#     volume = fields.Float("Volume", required=True)



class cuve(models.Model):
    _name = 'eaglefuel.cuve'
    _description = 'Cuve'
    # _rec_name = "ref"

    ref = fields.Char("reference", default="New")
    station_id = fields.Many2one("eaglefuel.station", string="station id")
    longeur_regle = fields.Char("Taille max régle")
    diametre = fields.Float("Diametre", required=True)
    hauteur = fields.Float("Hauteur", required=True)
    volume = fields.Float("Volume", compute='volume_cuve') #pi*rcarre*h
    jauge_id = fields.One2many("eaglefuel.jauge", "cuve_id", string="jauge")


    def name_get(self):
        result = []
        for cuve in self:
            name = str("[") + str(cuve.station_id.ref) +str("] ") + str(cuve.ref)
            result.append((cuve.id, name))
        return result

    def volume_cuve(self):
        for line in self:
            line.volume= ((line.diametre/2)**2)*line.hauteur*3.14

    @api.model
    def create(self, values):
        res = super(cuve, self).create(values)
        res.write({ref: f'{station_id}/{res.id}'})
        return res

    @api.model
    def create(self, values):
        values['ref'] = self.env['ir.sequence'].next_by_code('seq.cuve.ref') or _('New')
        return super(cuve, self).create(values)
