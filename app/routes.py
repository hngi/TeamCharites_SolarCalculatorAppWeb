from app import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/calculate")
def calculate():
    return render_template('calculate.html', title='Calculate')