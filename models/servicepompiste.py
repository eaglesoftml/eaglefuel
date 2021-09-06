#-*- coding: utf-8 -*-

from odoo import models, fields, api

class servicepompiste(models.Model):
    # _inherit = "eaglefuel.compteur"
    _name = "eaglefuel.servicepompiste"
    _description = "service pompiste"
    # _rec_name = "ref"

    ref = fields.Char("Reference")
    date = fields.Datetime("Date du service", required=True)
    shift = fields.Selection(selection=[('matin', 'Matin'),('soir', 'Soir')])
    # temps_debut = fields.Float("Heure de depart", required=True)
    # temps_fin = fields.Float("Heure de fin")
    # duree = fields.Float("Duree du service")
    # index_depart = fields.Integer("Index de depart")
    # index_arrive = fields.Integer("Index d'arrive")
    litrage_vendu = fields.Float("litres", compute="litrage_totals")
    litrage_credit = fields.Float()
    litres_gasoile_vendu = fields.Float("Gasoile vendu", compute="litrage_carb")
    litres_essence_vendu = fields.Float("Essence vendu", compute="litrage_carb")
    montant_credit = fields.Float()
    montant_total_vendu = fields.Float("Montant", compute="montant_carb")
    montant_gasoile = fields.Float()
    montant_essence = fields.Float()
    montant_a_verse = fields.Integer()
    montant_verse = fields.Integer()
    ecart = fields.Integer()
    montant = fields.Integer("Montant")
    qm_id = fields.Many2one("hr.employee", string="QM")
    pompiste_id = fields.Many2one("hr.employee", string="Pompiste")
    pompe_id = fields.Many2one("eaglefuel.pompe", string="pompe utilise")
    versement_id = fields.One2many("eaglefuel.versement", "servicepompiste_id", string="versement")
    station_id = fields.Many2one(related="pompe_id.ilo_id.station_id")
    detailventecarburant_id = fields.One2many("eaglefuel.detailventecarburant", "servicepompiste_id", string="detail su carburant vendus")
    releveindex_id = fields.One2many("eaglefuel.releveindex", "servicepompiste_id", string="releve index")

    def name_get(self):
        result = []
        for servicepompiste in self:
            name = str("[") + str(servicepompiste.pompe_id.ilo_id.station_id.ref) +str("] ") + str(servicepompiste.ref)
            result.append((servicepompiste.id, name))
        return result

    @api.depends('releveindex_id.litrage')
    def litrage_totals(self):
        for record in self:
            litrage_vendu = 0
            for line in record.releveindex_id:
                litrage_vendu += line.litrage
            record.update({'litrage_vendu': litrage_vendu})
        return litrage_vendu

    @api.depends('releveindex_id.litrage')
    def litrage_carb(self):
        for record in self:
            litres_essence_vendu = 0
            litres_gasoile_vendu = 0
            for line in record.releveindex_id:
                if line.carburant == "Essence":
                    litres_essence_vendu += line.litrage
                else:
                    litres_gasoile_vendu += line.litrage
            record.update({'litres_essence_vendu': litres_essence_vendu, 'litres_gasoile_vendu': litres_gasoile_vendu})
        # return litres_essence_vendu

    def montant_carb(self):
        for line in self:
            line.montant_total_vendu = line.litres_essence_vendu*663+line.litres_gasoile_vendu*593
    # def litrage_gasoile(self):
    #     for record in self:
    #         litres_gasoile_vendu = 0
    #         for line in record.releveindex_id:
    #             if line.carburant == "Gasoile":
    #                 litres_gasoile_vendu += line.litrage
    #         record.update({'litres_gasoile_vendu': litres_gasoile_vendu})
    #     return litres_gasoile_vendu

        # if line.releveindex_id.compteur_id.pistole_id.produit_servi == "e":
        #     line.litrage_essence = 10 #line.releveindex_id.litrage
        # else:
        #     line.litrage_gasoile = 100 #line.releveindex_id.litrage

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