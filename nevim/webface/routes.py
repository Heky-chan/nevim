from . import app
from flask import render_template


@app.route('/')
def index():
    pi=3.141519
    title = 'Index'
    return render_template('base.html.j2', pi=pi, title=title)


@app.route('/info/')
def info():
    title = 'Info'
    return render_template('info.html.j2', title=title)

@app.route('/květák/')
def květák():
    title = 'Květák'
    return render_template('květák.html.j2', title=title)

@app.route('/banány/')
def banány():
    title = 'Banány'
    return render_template('banány.html.j2', title=title)

@app.route('/kapusta/')
def kapusta():
    title = 'Kapusta'
    return render_template('kapusta.html.j2', title=title)