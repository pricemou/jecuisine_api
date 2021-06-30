# -*- coding: utf-8 -*-
{
    'name':
    "JeCuisine",
    'summary':
    """
        API for recipe app JeCuisine""",
    'description':
    """
        API for recipes and ingredients.
    """,
    'author':
    "AfricaDevTalents",
    'website':
    "http://www.AfricaDevTalents.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':
    'Recipes',
    'version':
    '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/recipe.xml',
        'views/ingredient.xml',
        'views/ingredientWithQty.xml',
        'views/quantity.xml',
        'views/category.xml',
        'views/origin.xml',
        'views/measurement.xml',
        'views/steps.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
