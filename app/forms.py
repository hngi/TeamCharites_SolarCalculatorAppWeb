from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from app.models import User
import re


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=5, max=20)])
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
    quantity = IntegerField('Quantity', validators=[DataRequired('Please enter a Number')])
    power = IntegerField('Power', validators=[DataRequired('Please enter a Number')])
    hours = IntegerField('Hours per Day', validators=[DataRequired('Please enter a Number'), NumberRange(max=24)])
    submit = SubmitField('Add')
