# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Measurement(models.Model):
    _name = 'jecuisine.measurement'
    _description = 'Model for measurement'
    _rec_name = "measure"

    measure = fields.Char(string="Unité de mesure", required=True)
    abreviation = fields.Char(string="Abréviation")
    description = fields.Text(string="Description")
