from odoo import models, fields, api

class cuve(models.Model):
    _name = "eaglefuel.cuve"
    _description = "cuve"

    station_id = fields.Many2one("eaglefuel.station", string="Station")
    container_ref = fields.Char("Ref citerne", required=True, index=True)
    capacite_volume = fields.Char("Capacite")
    longeur_regle = fields.Char("Taille max régle")
    ratioRV = fields.Float("Ratio Régle/Volume", required=True)
    position = fields.Char("Position", required=True)
    product_id = fields.Many2one("product.template", "Produit Stocké")   
    weight = fields.Float("Weight", required=True)
    volume = fields.Float("Volume", required=True)

    
    