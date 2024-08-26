from app import app
from flask import render_template

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
