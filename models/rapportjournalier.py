#-*- coding: utf-8 -*-

from odoo import models, fields, api

class rapportjournalier(models.Model):
    _name = "eaglefuel.rapportjournalier"
    _description = "rapport journalier desventes carburant"

    ref = fields.Char("Reference")
    date = fields.Date("date")
    essence = fields.Float(compute="litrage_vendu")
    gasoile = fields.Float(compute="litrage_vendu")
    total = fields.Float(compute="litrage_vendu")
    # essence_pompe = fields.Float(compute="litrage_vendu_pompe")
    # gasoile_pompe = fields.Float(compute="litrage_vendu_pompe")
    # total_pompe = fields.Float(compute="litrage_vendu_pompe")
    station_id = fields.Many2one("eaglefuel.station", "Station id")


    def name_get(self):
        result = []
        for rapport in self:
            name = str("[") + str(rapport.station_id.ref) +str("] ") + str(rapport.ref)
            result.append((rapport.id, name))
        return result

    @api.depends('station_id.pompe_id.servicepompiste_id.litres_essence_vendu','station_id.pompe_id.servicepompiste_id.litres_gasoile_vendu','station_id.pompe_id.servicepompiste_id.litrage_vendu')
    def litrage_vendu(self):
        for record in self:
            essence = 0
            gasoile = 0
            total = 0
            for line in record.station_id.pompe_id.servicepompiste_id:
                if line.date == record.date:
                    essence += line.litres_essence_vendu
                    gasoile += line.litres_gasoile_vendu
                    total += line.litrage_vendu
            record.update({'essence': essence,'gasoile':gasoile,'total':total})
        # return essence


    # @api.depends('station_id.pompe_id.servicepompiste_id.releveindex_id.date_releve','station_id.pompe_id.servicepompiste_id.releveindex_id.litrage')
    # def litrage_vendu_pompe(self):
    #     for record in self:
    #         total_pompe = 0
    #         for line in record.station_id.pompe_id.servicepompiste_id.releveindex_id:
    #             if record.date == line.date_releve:
    #                 total_pompe += line.litrage
    #     record.update({'total_pompe':total_pompe})

    # def aujourdhui(self):
    #     for line in self:
    #         line.ensure_one()
    #         line.date = fields.Datetime.now().strftime('%Y-%m-%d')
