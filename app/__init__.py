from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'horlla5791628be0c676dfde280ba245'

from app import routes