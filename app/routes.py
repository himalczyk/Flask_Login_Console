from flask import render_template, flash, redirect
from flask.helpers import url_for
from app.forms import LoginForm
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)