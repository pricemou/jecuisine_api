# -*- coding: utf-8 -*-
from odoo import http
import json
from math import *


class JecuisineApi(http.Controller):
    def convert_float_to_int(self, number):
        data = ceil(round(float(number) * 60, 2))
        return data

    def get_image_url(self, res_id, res_model):
        url = "/"
        query = "SELECT * FROM ir_attachment WHERE res_id ={} AND res_model='{}' ".format()
            int(res_id), res_model)
        http.request.env.cr.execute(query)
        attachment_found_id = http.request.env.cr.fetchone()[0]
        attachment = http.request.env['ir.attachment'].sudo().browse(
            attachment_found_id)
        if attachment.exists():
            if not attachment.public:
                attachment.write({"public": True})
            url = '/web/content/{}'.format(attachment_found_id)
        return url

    @http.route('/api/v1/recipes/<int:id>', auth='public', methods=['GET'])
    def get_recipes_details(self, id):
        data = {}
        all_ingredients = []
        all_steps = []
     recipe   found_recipe = http.request.env['jecuisine.recipe'].sudo().browse(id)
        if found_recipe.exists():
            status = 200
            for recipe in found_recipe:
                recipe_price = 0
                recipe_minute = 0
                # Loop to retrieve all ingredients in a single recipe
                for ingredient in recipe.ingredient_ids:
                    recipe_price += ingredient.price_total
                    found_ingredient = {
                        "id":
                        ingredient.id,
                        "name":
                        ingredient.ingredient.name,
                        "measure":
                        ingredient.measure.measure,
                        "qty":
                        ingredient.qty.qty,
                        "total_price":
                        ingredient.price_total,
                        "image":
                        self.get_image_url(ingredient.id,
                                           "jecuisine.ingredient.qty")
                    }
                    all_ingredients.append(found_ingredient)

                # Loop to retrieve all steps in a single recipe
                for step in recipe.steps_ids:
                    recipe_minute += self.convert_float_to_int(step.time)
                    found_step = {
                        "id": step.id,
                        "time": self.convert_float_to_int(step.time),
                        "description": step.description
                    }
                    all_steps.append(found_step)

                data = {
                    "id": recipe.id,
                    "name": recipe.name,
                    "category": recipe.category_id.name,
                    "origin": recipe.origin_id.name,
                    "ingredients": all_ingredients,
                    "steps": all_steps,
                    "recipe_price": recipe_price,
                    "recipe_minute": recipe_minute,
                    "status": status,
                    "message": "Success",
                    "image": self.get_image_url(recipe.id, "jecuisine.recipe")
                }

        else:
            data = {
                "status": 200,
                "message":
                "Aucune recette ne correspond à cet id: {}.".format(id)
            }
        result = json.dumps(data)
        return result

    @http.route('/api/v1/recipes', auth='public', methods=['GET'])
    def get_recipes(self):
        all_recipes = []
        data = {}
        arr_recipes = http.request.env['jecuisine.recipe'].sudo().search([])
        if arr_recipes.exists():
            status = 200
            message = "Success"
            for recipe in arr_recipes:
                recipe_price = 0
                recipe_minute = 0
                # Loop to calculate recipe price
                for ingredient in recipe.ingredient_ids:
                    recipe_price += ingredient.price_total

                # Loop to calculate recipe duration
                for step in recipe.steps_ids:
                    recipe_minute += self.convert_float_to_int(step.time)

                found_recipe = {
                    "id": recipe.id,
                    "name": recipe.name,
                    "category": recipe.category_id.name,
                    "origin": recipe.origin_id.name,
                    "ingredients": recipe.ingredient_ids.mapped("id"),
                    "steps": recipe.steps_ids.mapped("id"),
                    "recipe_price": recipe_price,
                    "recipe_minute": recipe_minute,
                    "image": self.get_image_url(recipe.id, "jecuisine.recipe")
                }
                all_recipes.append(found_recipe)
        else:
            status = 404
            message = "No recipe or error during data fetching !"
        data = {"result": all_recipes, "status": status, "message": message}
        result = json.dumps(data)
        return result
