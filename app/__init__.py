from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'horlla1628bb0b13ce0c676dfde280ba245'

from app import routes