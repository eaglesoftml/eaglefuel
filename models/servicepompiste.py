#-*- coding: utf-8 -*-

from odoo import models, fields, api

class servicepompiste(models.Model):
    # _inherit = "eaglefuel.compteur"
    _name = "eaglefuel.servicepompiste"
    _description = "service pompiste"
    # _rec_name = "ref"

    ref = fields.Char("Reference")
    date = fields.Date("Date", required=True)
    shift = fields.Selection(selection=[('matin', 'Matin'),('soir', 'Soir')])
    # temps_debut = fields.Float("Heure de depart", required=True)
    # temps_fin = fields.Float("Heure de fin")
    # duree = fields.Float("Duree du service")
    # index_depart = fields.Integer("Index de depart")
    # index_arrive = fields.Integer("Index d'arrive")
    litrage_vendu = fields.Float("litres", compute="litrage_totals")
    litrage_credit = fields.Float()
    litres_gasoile_vendu = fields.Float("Gasoile", compute="litrage_carb")
    litres_essence_vendu = fields.Float("Essence", compute="litrage_carb")
    montant_credit = fields.Float("Credit", compute="total_montant")
    montant_mobile = fields.Float("Mobile", compute="total_montant")
    montant_total_vendu = fields.Float("Montant", compute="montant_carb")
    montant_gasoile = fields.Float()
    montant_essence = fields.Float()
    montant_a_verse = fields.Integer()
    montant_verse = fields.Float("Montant verse", compute="total_montant")
    ecart = fields.Float("Ecart", compute="ecart_compte")
    montant = fields.Integer("Montant")
    qm_id = fields.Many2one("hr.employee", string="QM")
    pompiste_id = fields.Many2one("hr.employee", string="Pompiste")
    pompe_id = fields.Many2one("eaglefuel.pompe", string="pompe utilise")
    station_id = fields.Many2one(string="Station",related="pompe_id.station_id")
    releveindex_id = fields.One2many("eaglefuel.releveindex", "servicepompiste_id", string="releve index")
    paiement_id = fields.One2many("eaglefuel.paiement", 'servicepompiste_id',string="Paiement")

    def name_get(self):
        result = []
        for servicepompiste in self:
            name = str("[") + str(servicepompiste.pompe_id.station_id.ref) +str("] ") + str(servicepompiste.ref)
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
    #
    #     if line.releveindex_id.compteur_id.pistole_id.produit_servi == "e":
    #         line.litrage_essence = 10 #line.releveindex_id.litrage
    #     else:
    #         line.litrage_gasoile = 100 #line.releveindex_id.litrage

    @api.depends('versement_id.montant_versement')
    def total_verse(self):
        for record in self:
            montant_verse = 0
            for line in record.versement_id:
                montant_verse += line.montant_versement
            record.update({'montant_verse': montant_verse})
        return montant_verse

    @api.depends('paiement_id.montant')
    def total_montant(self):
        for record in self:
            montant_credit = 0
            montant_verse = 0
            montant_mobile = 0
            for line in record.paiement_id:
                if line.type == 'b':
                    montant_credit += line.montant
                elif line.type == 'a':
                    montant_verse += line.montant
                elif line.type == 'c':
                    montant_mobile += line.montant
            record.update({'montant_credit': montant_credit,'montant_verse': montant_verse,'montant_mobile': montant_mobile})
        #return montant_credit


    def ecart_compte(self):
        for line in self:
            line.montant_a_verse = line.montant_total_vendu-line.montant_credit-line.montant_mobile
            line.ecart = line.montant_a_verse-line.montant_verse


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