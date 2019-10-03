from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm, LoginForm, ApplianceForm, OutputForm
from app.models import User, Appliance
from flask_login import login_user, current_user, logout_user, login_required
import math

suggest = {
    "Coffee Pot": 200,
    "Coffee Maker": 800,
    "Toaster": 1500,
    "Blender": 300,
    "Microwave": 1500,
    "Hot Plate": 1200,
    "Dishwasher": 1500,
    "Washing Machine": 500,
    "Iron": 1000,
    "Electric Heater": 1500,
    "Air conditioner": 1000,
    "Ceiling Fan": 50,
    "Computer (Laptop)": 50,
    "Computer (Desktop)": 150,
    "Computer Printer": 100,
    "TV (25in Color)": 150,
    "TV (19in Color)": 70,
    "TV (12in B/W)": 20,
    "CD Player": 35,
    "Stereo": 30,
    "Satellite Dish": 30,
    "Lights (100W Incandescent)": 100,
    "Lights (25W Compact Flourescent)": 28,
    "Lights (50W DC Incandescent)": 50,
    "Refrigerator": 100
}

@app.route("/")
@app.route('/home')
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/FAQ")
def FAQ():
    return render_template('FAQ.html')


@app.route("/calculate", methods=['GET', 'POST'])
@login_required
def calculate():
    return render_template('calculate.html')

@app.route("/get_result")
def get_result():
    return render_template('get_result.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        data = request.form
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        user = User(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        data = request.form
        user = User.query.filter_by(email=data['username']).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404


@app.errorhandler(403)
def error_403(error):
    return render_template('403.html'), 403

@app.errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500

@app.route("/output", methods=['GET', 'POST'])
@login_required
def output():
    appliances = Appliance.query.filter_by(owner=current_user)
    appliance_totals = [0]
    for appliance in appliances:
        appliance_totals.append(appliance.total)
    output = sum(appliance_totals)
    form = ApplianceForm()
    if form.validate_on_submit():
        name = form.name.data
        quantity = form.quantity.data 
        power = form.power.data
        hours = form.hours.data
        total = (quantity*power*hours)
        owner = current_user
        appliance = Appliance(name=name, quantity=quantity, power=power, hours=hours, total=total, owner=owner)
        db.session.add(appliance)
        db.session.commit()
        flash('You have added an appliance', 'success')
        return redirect(url_for('output'))
    return render_template('output.html', form=form, output=output, appliances=appliances, suggest=suggest)

@app.route("/appliance/<int:appliance_id>/delete", methods=['POST'])
@login_required
def delete(appliance_id):
    appliance = Appliance.query.get_or_404(appliance_id)
    if appliance.owner != current_user:
        abort(403)
    db.session.delete(appliance)
    db.session.commit()
    flash('Your appliance has been deleted!', 'success')
    return redirect(url_for('output'))