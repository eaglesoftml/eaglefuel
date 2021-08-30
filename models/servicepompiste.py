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
