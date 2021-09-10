#-*- coding: utf-8 -*-

from odoo import models, fields, api

class rapportjournalier(models.Model):
    _name = "eaglefuel.rapportjournalier"
    _description = "rapport journalier desventes carburant"

    date = fields.Date("date")
    essence = fields.Float(compute="litrage_vendu")
    gasoile = fields.Float(compute="litrage_vendu")
    total = fields.Float(compute="litrage_vendu")
    station_id = fields.Many2one("eaglefuel.station", "Station id")

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

