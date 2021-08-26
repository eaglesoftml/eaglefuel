#-*- coding: utf-8 -*-

from odoo import models, fields, api

class servicepompiste(models.Model):
    _name = "eaglefuel.servicepompiste"
    _description = "service pompiste"

    date = fields.Datetime("Date du service", required=True)
    temps_debut = fields.Float("Heure de depart", required=True)
    temps_fin = fields.Float("Heure de fin")
    duree = fields.Float("Duree du service")

    # qm_id = fields.Many2many("hr.employee", string="QM_responsables")
    # pompiste_id = fields.Many2one("hr.employee", string="Pompiste responsable")
    ilo_id = fields.Many2one("eaglefuel.ilo", string="Ilo utilise")
    versement_id = fields.One2many("eaglefuel.versement", "servicepompiste_id", string="versement")



class versement(models.Model):
    _name = "eaglefuel.versement"
    _description = "versement"
    _inherit = "eaglefuel.compteur"

    montant_versement = fields.Integer("Montant du versement")
    heure_versement = fields.Float("Heure du versement", required=True)
    nbre_versement = fields.Integer("Nombre de versement")
    total_versement = fields.Integer("Total somme verse")
    servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste", string="service pompiste")



