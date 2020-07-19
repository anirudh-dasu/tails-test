import os
from flask import current_app, url_for
import json


class Store:
	name = None
	postcode = None

	def __init__(self, name, postcode):
		self.name = name
		self.postcode = postcode

	def __repr__(self):
		return '<Store {} {}>'.format(self.name, self.postcode)


class StoreDataLoader:
	
	def load_data(self, search_string, limit, offset):
		filename = os.path.join(current_app.static_folder, current_app.config['STORES_FILE'])
		data = self.read_file(filename)
		if (search_string and search_string.strip()):
			data = self.filter(data, search_string)
		return data[offset:(limit + offset)]

	def filter(self, stores_list, search_string):
		search_string = search_string.lower()
		return [d for d in stores_list if ((search_string in d['postcode'].lower()) or search_string in d['name'].lower())]
	
	def read_file(self, filename):
		with open(filename) as stores_file:
			data = json.loads(stores_file.read())
		return data