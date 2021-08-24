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

    pompe_number = fields.Integer("Numero de pompe", required=True)
    nom = fields.Char("Reference de la pompe")
    description = fields.Text()

    ilo_id = fields.Many2one("eaglefuel.ilo", "Ilo parent")
    pistole_id = fields.One2many("eaglefuel.pistole", "pompe_id", string="pistole")
    compteur_id = fields.One2many("eaglefuel.compteur", "pompe_id", string="compteur")
        
    