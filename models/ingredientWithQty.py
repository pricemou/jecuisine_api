# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models


class IngredientWithQty(models.Model):
    _name = 'jecuisine.ingredient.qty'
    _description = 'Model for ingredient with qty'
    _rec_name = "fullname"

    ingredient = fields.Many2one(comodel_name='jecuisine.ingredient',
                                 string='Nom ingredient', required=True)
    qty = fields.Many2one(comodel_name='jecuisine.quantity',
                          string='Quantité', required=True)
    measure = fields.Many2one(
        comodel_name='jecuisine.measurement', string='Unité de mesure', required=True, compute="_get_measure")

    image = fields.Binary(string='Image', attachment=True,
                          help="Ce champ va contenir l'image de l'ingredient limitée à 400x400px.", related="ingredient.image", store=True)

    fullname = fields.Char(string='Nom complet', compute="_get_fullname")
    recipe_id = fields.Many2one(
        comodel_name='jecuisine.recipe', string='Recipe id')

    price_total = fields.Float(
        string='Montant total', readonly=True, compute="_get_amount_total")

    @api.depends('ingredient', 'qty')
    def _get_amount_total(self):
        for rec in self:
            rec.price_total = float(rec.ingredient.price * rec.qty.qty)

    @api.depends('ingredient', "qty", "measure")
    def _get_fullname(self):
        for rec in self:
            rec.fullname = "{}-{}-{}".format(rec.ingredient.name,
                                             rec.qty.qty, rec.measure.measure)

    @api.depends('ingredient')
    def _get_measure(self):
        for rec in self:
            rec.measure = rec.ingredient.measure
