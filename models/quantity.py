# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Ingredient(models.Model):
    _name = 'jecuisine.quantity'
    _description = 'Model for quantity'
    _rec_name = "qty"

    qty = fields.Float(string="Quantité", required=True)
