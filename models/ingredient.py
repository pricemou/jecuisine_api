# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models, tools, modules


class Ingredient(models.Model):
    _name = 'jecuisine.ingredient'
    _description = 'Model for ingredient'
    _rec_name = "fullname"

    name = fields.Char(string="Nom", required=True)
    price = fields.Float(string='Prix unitaire', default=0, required=True)
    description = fields.Text(string='Description')
    measure = fields.Many2one(
        comodel_name='jecuisine.measurement', string='Unité de mesure', required=True)

    # Put before calling function Get default image for recipe
    def _get_default_image(self):
        image_path = modules.get_module_resource(
            'jecuisine_api', 'static/src/img', 'placeholder.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    image = fields.Binary(string='Image', attachment=True,
                          help="Ce champ va contenir l'image de l'ingredient limitée à 400x400px.", default=_get_default_image)
    fullname = fields.Char(string='Nom complet', compute="_get_fullname")

    @api.depends("name", "measure")
    def _get_fullname(self):
        for rec in self:
            rec.fullname = "{}- ({})".format(rec.name, rec.measure.measure)
