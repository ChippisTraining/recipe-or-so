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

data = {
    '101': {
        'info': {
            'thumbnail': '114/recipes/101.jpeg',
            'title': 'Spiced Ground Beef with Mushrooms',
            'description': 'A pan filled with spiced ground beef, mushrooms, and onions cooked on a stove.',
            'prep-time': 10,
            'cook-time': 20,
            'servings': 4,
            'tags': [
                'Beef',
                'Dinner',
                'Mushrooms',
                'Spicy',
                'Food'
            ]
        },
        'instructions': [
            {'title': 'STEP 1', 'body': 'Heat a large skillet over medium heat. Add ground beef and cook until browned, breaking it up as it cooks.'},
            {'title': 'STEP 2', 'body': 'Add sliced mushrooms and onions to the skillet. Sauté until softened, stirring occasionally.'},
            {'title': 'STEP 3', 'body': 'Season with salt, pepper, and your choice of spices. Serve hot over rice or with bread.'}
        ],
        'ingredients': [
            '500g ground beef',
            '1 cup sliced mushrooms',
            '1/2 cup diced onions',
            'Salt and pepper to taste',
            '1 tsp paprika'
        ],
        'tools': [
            'Large Skillet',
            'Wooden Spoon'
        ]
    },
    '102': {
        'info': {
            'thumbnail': '144/recipes/102.jpeg',
            'title': 'Herb-Crusted Rack of Lamb',
            'description': 'A perfectly roasted rack of lamb with a crispy herb crust, placed on a dark slate serving board.',
            'prep-time': 15,
            'cook-time': 25,
            'servings': 4,
            'tags': [
                'Lamb',
                'Dinner',
                'Gourmet',
                'BBQ',
                'Food'
            ]
        },
        'instructions': [
            {'title': 'STEP 1', 'body': 'Preheat the oven to 200°C (400°F). Season the rack of lamb with salt and pepper.'},
            {'title': 'STEP 2', 'body': 'Mix chopped herbs, garlic, and breadcrumbs. Coat the lamb with Dijon mustard, then press the herb mixture onto the surface.'},
            {'title': 'STEP 3', 'body': 'Roast in the oven for 20-25 minutes or until desired doneness. Let rest before slicing and serving.'}
        ],
        'ingredients': [
            '1 rack of lamb',
            '2 tbsp Dijon mustard',
            '1/2 cup breadcrumbs',
            '2 tbsp chopped parsley',
            '1 tbsp minced garlic'
        ],
        'tools': [
            'Oven',
            'Baking Tray'
        ]
    },
    '103': {
        'info': {
            'thumbnail': '144/recipes/103.jpeg',
            'title': 'Caramel Drizzled Pancakes with Berries',
            'description': 'A stack of fluffy pancakes topped with caramel sauce, fresh strawberries, and chopped nuts, served with whipped cream on the side.',
            'prep-time': 10,
            'cook-time': 15,
            'servings': 6,
            'tags': [
                'Breakfast',
                'Pancakes',
                'Dessert',
                'Food'
            ]
        },
        'instructions': [
            {'title': 'STEP 1', 'body': 'In a mixing bowl, combine the dry pancake mix and flax seed meal. Gradually add the skim milk, stirring continuously until a smooth batter forms.'},
            {'title': 'STEP 2', 'body': 'Preheat a large heavy pot with a lid over medium heat. Lightly grease the surface and pour in small amounts of batter to form pancakes. Cook until bubbles form on the surface, then flip and cook until golden brown.'},
            {'title': 'STEP 3', 'body': 'Stack the cooked pancakes on a plate. Drizzle caramel sauce over them, top with fresh strawberries and chopped nuts, and serve with whipped cream on the side.'}
        ],
        'ingredients': [
            '1 1/2 cups dry pancake mix',
            '1/2 cup flax seed meal',
            '1 cup skim milk',
            'Caramel sauce',
            'Fresh strawberries'
        ],
        'tools': [
            'Hand Blender',
            'Large Heavy Pot With Lid'
        ]
    },
    '104': {
        'info': {
            'thumbnail': '114/recipes/104.jpeg',
            'title': 'Creamy Tomato Basil Soup',
            'description': 'A bowl of smooth tomato soup garnished with fresh basil, served with bread on the side.',
            'prep-time': 10,
            'cook-time': 30,
            'servings': 4,
            'tags': [
                'Soup',
                'Vegan',
                'Comfort Food',
                'Food'
            ]
        },
        'instructions': [
            {'title': 'STEP 1', 'body': 'In a large pot, sauté onions and garlic until fragrant. Add chopped tomatoes and cook until softened.'},
            {'title': 'STEP 2', 'body': 'Pour in vegetable broth and let simmer for 20 minutes. Blend until smooth and stir in fresh basil and cream (optional).'},
            {'title': 'STEP 3', 'body': 'Serve hot with crusty bread on the side, garnished with extra basil leaves.'}
        ],
        'ingredients': [
            '1 can chopped tomatoes',
            '1 cup vegetable broth',
            '1/2 cup chopped onions',
            '1 clove garlic, minced',
            'Fresh basil leaves'
        ],
        'tools': [
            'Blender',
            'Large Pot'
        ]
    }
}

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
    return render_template('tags.html', tag_data=tag_data)

@public.route('/recipes')
def recipes():
    return render_template('recipes.html', tag_data=tag_data, recipes_data=recipes_data)

@public.route('/recipe/<id>/<title>/')
def recipe(id: int, title: str):
    return render_template('single-recipe.html', recipe=data.get(str(id)))

@public.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', recipes_data=recipes_data)

