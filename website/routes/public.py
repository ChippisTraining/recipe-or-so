from flask import Blueprint, render_template
import os

public = Blueprint('public', __name__, template_folder='templates')

@public.route('/')
def index():
    tag_data = [
        {"tag": "pizza", "title": "Pizza", "count": 12},
        {"tag": "pasta", "title": "Pasta", "count": 8},
        {"tag": "salad", "title": "Salad", "count": 5},
        {"tag": "dessert", "title": "Dessert", "count": 10},
        {"tag": "vegan", "title": "Vegan", "count": 4},
        {"tag": "bbq", "title": "BBQ", "count": 6},
        {"tag": "seafood", "title": "Seafood", "count": 0},
        {"tag": "breakfast", "title": "Breakfast", "count": 0}
    ]

    return render_template('index.html', tag_data=tag_data)

@public.route('/about')
def about():
    return render_template('about.html')

@public.route('/tags')
def tags():
    return render_template('tags.html')

@public.route('/recipes')
def recipes():
    return render_template('recipes.html')

@public.route('/recipe/<id>/<author>/')
def recipe(id: int, author: str):
    return render_template('single-recipe.html')

@public.route('/contact')
def contact():
    return render_template('contact.html')

