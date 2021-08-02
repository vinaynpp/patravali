from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required


auth = Blueprint(name='auth', import_name=__name__, static_folder='static', static_url_path='static',
                 template_folder='templates')
@auth.route('/')
def index():
    return "asdgsdhbsdzh"

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')