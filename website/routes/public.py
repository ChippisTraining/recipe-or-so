from flask import Blueprint, render_template

public = Blueprint('public', __name__, template_folder='templates')

@public.route('/')
def index():
    return render_template('index.html')

@public.route('/about')
def about():
    return render_template('index.html')

@public.route('/tags')
def tags():
    return render_template('index.html')

@public.route('/recipes')
def recipes():
    return render_template('index.html')

@public.route('/contact')
def contact():
    return render_template('index.html')
