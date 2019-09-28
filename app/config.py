import os
from app import routes

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = 'horlla5791628be0c676dfde280ba245'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')