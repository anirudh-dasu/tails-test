import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-key'
	STORES_FILE = 'stores.json'
	POSTCODES_URL = 'http://api.postcodes.io/postcodes'
