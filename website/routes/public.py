from flask import Blueprint, render_template, request
import os

public = Blueprint('public', __name__, template_folder='templates')

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
        'url-title': 'Spiced Ground Beef with Mushrooms'.replace(' ', '-').lower(),
        'thumbnail': '114/recipes/101.jpeg',
        'alt-text': 'A pan filled with spiced ground beef, mushrooms, and onions cooked on a stove.',
        'prep-time': 10,
        'cook-time': 20
    },
    {
        'id': 102,
        'title': 'Herb-Crusted Rack of Lamb',
        'url-title': 'Herb-Crusted Rack of Lamb'.replace(' ', '-').lower(),
        'thumbnail': '144/recipes/102.jpeg',
        'alt-text': 'A perfectly roasted rack of lamb with a crispy herb crust, placed on a dark slate serving board.',
        'prep-time': 15,
        'cook-time': 25
    },
    {
        'id': 103,
        'title': 'Caramel Drizzled Pancakes with Berries',
        'url-title': 'Caramel Drizzled Pancakes with Berries'.replace(' ', '-').lower(),
        'thumbnail': '144/recipes/103.jpeg',
        'alt-text': 'A stack of fluffy pancakes topped with caramel sauce, fresh strawberries, and chopped nuts, served with whipped cream on the side.',
        'prep-time': 10,
        'cook-time': 15
    },
    {
        'id': 104,
        'title': 'Creamy Tomato Basil Soup',
        'url-title': 'Creamy Tomato Basil Soup'.replace(' ', '-').lower(),
        'thumbnail': '114/recipes/104.jpeg',
        'alt-text': 'A bowl of smooth tomato soup garnished with fresh basil, served with bread on the side.',
        'prep-time': 10,
        'cook-time': 30
    }
]

@public.route('/')
def index():
    ctr = request.values.get('no', None)
    return render_template('index.html', tag_data=tag_data, recipes_data=[] if ctr else recipes_data)

@public.route('/about')
def about():
    return render_template('about.html', recipes_data=recipes_data)

@public.route('/tag/<tag>')
def tags_template(tag: str):
    return render_template('tag-template.html', chosen_tag=tag, recipes_data=recipes_data)

@public.route('/tags')
def tags():
    return render_template('tags.html', tag_data=recipes_data)

@public.route('/recipes')
def recipes():
    return render_template('recipes.html', tag_data=tag_data, recipes_data=recipes_data)

@public.route('/recipe/<id>/<title>/')
def recipe(id: int, title: str):
    return render_template('single-recipe.html')

@public.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', recipes_data=recipes_data)

