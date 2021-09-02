#-*- coding: utf-8 -*-

from odoo import models, fields, api

class servicepompiste(models.Model):
    # _inherit = "eaglefuel.compteur"
    _name = "eaglefuel.servicepompiste"
    _description = "service pompiste"
    # _rec_name = "ref"

    ref = fields.Char("Reference")
    date = fields.Datetime("Date du service", required=True)
    # temps_debut = fields.Float("Heure de depart", required=True)
    # temps_fin = fields.Float("Heure de fin")
    # duree = fields.Float("Duree du service")
    # index_depart = fields.Integer("Index de depart")
    # index_arrive = fields.Integer("Index d'arrive")
    litrage = fields.Float()
    litrage_credit = fields.Float()
    litage_gasoile = fields.Float()
    litage_essence = fields.Float()
    montant_credit = fields.Float()
    montant_total_vendu = fields.Integer()
    montant_gasoile = fields.Integer()
    montant_essence = fields.Integer()
    montant_a_verse = fields.Integer()
    montant_verse = fields.Integer()
    ecart = fields.Integer()

    qm_id = fields.Many2one("hr.employee", string="QM")
    pompiste_id = fields.Many2one("hr.employee", string="Pompiste")
    pompe_id = fields.Many2one("eaglefuel.pompe", string="pompe utilise")
    versement_id = fields.One2many("eaglefuel.versement", "servicepompiste_id", string="versement")
    station_id = fields.Many2one(related="pompe_id.ilo_id.station_id")
    detailventecarburant_id = fields.One2many("eaglefuel.detailventecarburant", "servicepompiste_id", string="detail su carburant vendus")


    def name_get(self):
        result = []
        for servicepompiste in self:
            name = str("[") + str(servicepompiste.pompe_id.ilo_id.station_id.ref) +str("] ") + str(servicepompiste.ref)
            result.append((servicepompiste.id, name))
        return result


# class detailventecarburant(models.Model):
#     _name = "eaglefuel.detailventecarburant"
#     _description = "detail des ventes du carburant"
#
#     nom_carb = fields.Char("Carburant")
#     servicepompiste_id = fields.Many2one("eaglefuel.servicepompiste",  string="releve index")
#
#     # def choisir_produit(self):
#     #     for line in self:
#     #         line.nom_carb = detailventecarburant.releveindex_id.