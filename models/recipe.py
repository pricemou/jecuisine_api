# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models, tools, modules


class Recipe(models.Model):
    _name = 'jecuisine.recipe'
    _description = 'Model for recipe app'

    name = fields.Char(string='Nom de la recette', required=True)
    description = fields.Text(string='Description')

    # Put before calling function Get default image for recipe
    def _get_default_image(self):
        image_path = modules.get_module_resource('jecuisine_api',
                                                 'static/src/img',
                                                 'cooking_pot_filled.png')
        return tools.image_resize_image_big(
            base64.b64encode(open(image_path, 'rb').read()))

    image = fields.Binary(
        string='Image',
        attachment=True,
        help=
        "Ce champ va contenir l'image de la recette limitée à 1024x1024px.",
        default=_get_default_image)

    ingredient_ids = fields.One2many(comodel_name='jecuisine.ingredient.qty',
                                     inverse_name='recipe_id',
                                     string='Ingredients')

    steps_ids = fields.One2many(comodel_name='jecuisine.steps',
                                inverse_name='recipe_id',
                                string='Étapes')

    category_id = fields.Many2one(comodel_name='jecuisine.category',
                                  string='Catégorie',
                                  required=True)
                                  
    origin_id = fields.Many2one(comodel_name='jecuisine.origin',
                                string='Origine',
                                required=True)
