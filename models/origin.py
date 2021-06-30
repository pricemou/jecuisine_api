# -*- coding: utf-8 -*-
from odoo import api, fields, models


class OriginJecuisine(models.Model):
    _name = 'jecuisine.origin'
    _description = 'Model for origin'

    name = fields.Char(string="Nom", required=True)
    description = fields.Text(string="Description")
