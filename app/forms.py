from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
import re


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        username = username.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
        elif len(username) < 5:
            raise ValidationError('Username must be at least 5 characters long')
        elif re.match(r'[A-Za-z0-9_]', username):
            raise ValidationError('Username should be a combination of lowercase and uppercase alphabetic characters, numeric characters and underscore')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

    def validate_password(self, password):
        password = password.data
        if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            pass
        else:
            raise ValidationError('Password must be more than 8 characters long and must contain uppercase alphabetic character(s), lowercase alphabetic character(s), numeric character(s) and symbol(s)')

class LoginForm(FlaskForm):
    login_data = StringField('Username/Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ApplianceForm(FlaskForm):
    name = StringField('Appliance', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    power = IntegerField('Power', validators=[DataRequired()])
    hours = IntegerField('Hours per Day', validators=[DataRequired()])
    submit = SubmitField('Add')

class OutputForm(FlaskForm):
    submit = SubmitField('Calculate')