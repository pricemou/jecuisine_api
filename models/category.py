# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CategoryJecuisine(models.Model):
    _name = 'jecuisine.category'
    _description = 'Model for category'

    name = fields.Char(string="Nom", required=True)
    description = fields.Text(string="Description")
