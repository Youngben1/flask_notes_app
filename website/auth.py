from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
            else:
                flash('Incorrect password, olodo try again', category='error')
        else:
            flash('This Email does not exist.', category='error')

    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout Page</p>"

@auth.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists, who account you want hack', category='error')
        elif len(email) < 5:
            flash('The Email correct for your eye so??', category='error')
        elif len(first_name) < 3:
            flash('First Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Why your passwords no de match olodo!!', category='error')
        elif len(password1) < 7:
            flash('Na your papa you de give short password', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully, their daddies!!!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html")