from flask import render_template
from app import app
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home PageTwopac Daht Space ')


@app.route('/blog')
def blog():
    user = {'username': 'mark'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Squid'},
            'body': 'bubble bbbubbblleee!'
        }
    ]
    return render_template('blog.html', title='Blog PageTwopac Daht Space ', user=user, posts=posts)


@app.route('/synth')
def synth():
    user = {'username': 'synth user'}
    return render_template('synth.html', title='Synth Project', user=user)
