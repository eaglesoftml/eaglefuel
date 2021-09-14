#-*- coding: utf-8 -*-

from odoo import models, fields, api

class jauge(models.Model):
    _name = 'eaglefuel.jauge'
    _description = "jauge"
    # _rec_name = "ref"

    ref = fields.Char("reference")
    mesure_regle = fields.Float("mesure regle", required=True)
    date_jauge = fields.Datetime("Date du jauge", required=True)
    litrage_jauge = fields.Integer("Litrage jauge")
    cuve_id = fields.Many2one("eaglefuel.cuve", string="cuve")
    employe_id= fields.Many2many("hr.employee", string="QM responsable")
    shift = fields.Selection(selection=[('matin', 'Matin'),('soir', 'Soir')])


    def name_get(self):
        result = []
        for jauge in self:
            name = str("[") + str(jauge.cuve_id.station_id.ref) +str("] ") + str(jauge.ref)
            result.append((jauge.id, name))
        return result