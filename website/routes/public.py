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
    
    recipes_data = [
    {
        'id': 101,
        'title': 'Spiced Ground Beef with Mushrooms',
        'thumbnail': '<user id>/recipes/recipe-1.jpeg',
        'alt_text': 'A pan filled with spiced ground beef, mushrooms, and onions cooked on a stove.',
        'prep_time': 10,
        'cook_time': 20
    },
    {
        'id': 102,
        'title': 'Creamy Tomato Basil Soup',
        'thumbnail': '<user id>/recipes/recipe-2.jpeg',
        'alt_text': 'A bowl of smooth tomato soup garnished with fresh basil, served with bread on the side.',
        'prep_time': 10,
        'cook_time': 30
    },
    {
        'id': 103,
        'title': 'Herb-Crusted Rack of Lamb',
        'thumbnail': '<user id>/recipes/recipe-3.jpeg',
        'alt_text': 'A perfectly roasted rack of lamb with a crispy herb crust, placed on a dark slate serving board.',
        'prep_time': 15,
        'cook_time': 25
    },
    {
        'id': 104,
        'title': 'Caramel Drizzled Pancakes with Berries',
        'thumbnail': '<user id>/recipes/recipe-4.jpeg',
        'alt_text': 'A stack of fluffy pancakes topped with caramel sauce, fresh strawberries, and chopped nuts, served with whipped cream on the side.',
        'prep_time': 10,
        'cook_time': 15
    }
]

    return render_template('index.html', tag_data=tag_data, recipes_data=recipes_data)

@public.route('/about')
def about():
    return render_template('about.html')

@public.route('/tags')
def tags():
    return render_template('tags.html')

@public.route('/recipes')
def recipes():
    return render_template('recipes.html')

@public.route('/recipe/<id>/<title>/')
def recipe(id: int, title: str):
    return render_template('single-recipe.html')

@public.route('/contact')
def contact():
    return render_template('contact.html')

