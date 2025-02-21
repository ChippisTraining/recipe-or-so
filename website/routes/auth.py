from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from ..forms.auth import SignupForm, LoginForm
from ..models.user import User
from .. import db

auth = Blueprint('auth', __name__, template_folder='templates/auth')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')

        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
            return redirect(url_for('auth.signup'))

        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash(f"Welcome, {new_user.username}!", "success")

        return redirect(url_for('public.index'))
    
    return render_template("auth/register.html", form=form)


# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for('public.index'))
        
        flash("Invalid credentials!", "danger")
    
    return render_template("auth/login.html", form=form)

# Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out!", "info")
    return redirect(url_for('public.index'))