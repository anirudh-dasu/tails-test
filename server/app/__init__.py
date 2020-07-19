import logging
from flask import Flask
from flask_cors import CORS
from config import Config



def create_app(config_class=Config):
	# Basic app setup
	app = Flask(__name__)
	CORS(app, resources={r'/*': {'origins': '*'}})
	app.config.from_object(config_class)

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)
	
	# Set up logging to STDOUT
	stream_handler = logging.StreamHandler()
	stream_handler.setLevel(logging.INFO)
	app.logger.addHandler(stream_handler)

	app.logger.setLevel(logging.INFO)
	app.logger.info('Tails-test startup')

	return app

from app import models
