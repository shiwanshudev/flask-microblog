from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ram Kumar'}
    posts = [
        {
            'author': {'username': 'Leo'},
            'body': 'It is a beautiful day!'
        },
        {
            'author': {'username': 'Mia'},
            'body': 'Just finished a great workout!'
        },
        {
            'author': {'username': 'Noah'},
            'body': 'Loving this new book I started.'
        },
        {
            'author': {'username': 'Ava'},
            'body': 'Had an amazing coffee this morning!'
        },
        {
            'author': {'username': 'Ethan'},
            'body': 'Excited for the weekend plans!'
        },
        {
            'author': {'username': 'Sophia'},
            'body': 'Enjoying a peaceful evening walk.'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html',title='Sign In', form=form)