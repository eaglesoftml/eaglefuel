#-*- coding: utf-8 -*-

from odoo import models, fields, api

class servicepompiste(models.Model):
    # _inherit = "eaglefuel.compteur"
    _name = "eaglefuel.servicepompiste"
    _description = "service pompiste"
    _rec_name = "ref"

    ref = fields.Char("reference")
    date = fields.Datetime("Date du service", required=True)
    temps_debut = fields.Float("Heure de depart", required=True)
    temps_fin = fields.Float("Heure de fin")
    duree = fields.Float("Duree du service")
    index_depart = fields.Integer("Index de depart")
    index_arrive = fields.Integer("Index d'arrive")
    litrage = fields.Float("Litrage vendu")
    litrage_credit = fields.Float("Litrage vendu a credit")
    montant_credit = fields.Float("Somme d'argent a credit")
    montant_total_vendu = fields.Integer("Total vendu")
    montant_a_verse = fields.Integer("Montant a verse")
    montant_verse = fields.Integer("Montant verse")
    ecart = fields.Integer("Ecart du compte")
    qm_id = fields.Many2many("hr.employee", string="QM_responsables")
    pompiste_id = fields.Many2one("hr.employee", string="Pompiste responsable")
    pompe_id = fields.Many2one("eaglefuel.pompe", string="pompe utilise")
    versement_id = fields.One2many("eaglefuel.versement", "servicepompiste_id", string="versement")

    def name_get(self):
        result = []
        for servicepompiste in self:
            name = str("[") + str(servicepompiste.pompe_id.ilo_id.station_id.ref) +str("] ") + str(servicepompiste.ref)
            result.append((servicepompiste.id, name))
        return result
