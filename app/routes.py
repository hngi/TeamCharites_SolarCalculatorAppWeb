from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route('/home')
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/calculate")
def calculate():
    return render_template('calculate.html', title='Calculate')


@app.route("/result")
def result():
    return render_template('results.html', title='Result')

# @app.route('/power_consumption', methods=['POST'])
# def total_output_load():
#     output = []
#     data = request.get_json()
#     for item in data:
#         app_qtty = item['qtty']
#         app_hours = item['hours']
#         app_consumption = item['consumption']
#         app_output = app_qtty * app_hours * app_consumption
#         output.append(app_output)
#     total_app_output = adder(output)
#     result = {'status': 'oK', 'status_code': '200', 'total_power_consumption': total_app_output}
#     return jsonify(result)
#
@app.route("/register", methods=['POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        data = request.form
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=data['username'], email=data['email'],password=hashed_password)
        # user = User(username=form.username.data, email=form.email.data, password=hashed_password)
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
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
#
# @app.errorhandler(404)
# def error_404(error):
#     return render_template('404.html'), 404
#
# @app.errorhandler(403)
# def error_403(error):
#     return render_template('404.html'), 403
#
# @app.errorhandler(500)
# def error_500(error):
#     return render_template('404.html'), 500