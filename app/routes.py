from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dawid'}
    posts = [
        {
            'author' : {'username': 'John'},
            'body' : 'Great day in Warsaw here in Poland!'
        },
        {
            'author': {'username': 'Susan'},
            'body' : 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Kamil'},
            'body' : 'Nice in here'
        },
        {
            'author': {'username': 'Adrina'},
            'body' : 'Woork!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)