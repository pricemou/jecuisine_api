# -*- coding: utf-8 -*-
from odoo import api, fields, models


class RecipeSteps(models.Model):
    _name = 'jecuisine.steps'
    _description = 'Model for steps'
    _rec_name = "time"

    time = fields.Float(string='Minutes', required=True, default=0)
    description = fields.Text(string='Description')
    recipe_id = fields.Many2one(
        comodel_name='jecuisine.recipe', string='Recipe id')
