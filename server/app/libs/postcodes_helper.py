import json
import requests
from flask import current_app

class PostcodesHelper():
	

	def __init__(self):
		self.postcodes_url = current_app.config['POSTCODES_URL']
		self.conn = requests.session()
		self.conn.headers = {'Content-Type': 'application/json'}
		
	def fetch_postcode_details(self, data):
		response = self.make_request(self.postcodes_url, 'POST', self.request_body(data))
		return self.pluck_lat_long(response)

	def pluck_lat_long(self, response):
		return [{'postcode': d['query'], 
		'latitude': (d.get('result', {}).get('latitude', None)), 
		'longitude': (d.get('result', {}).get('longitude',None))} 
		for d in response['result']]

	def request_body(self, data):
		return {"postcodes": [d['postcode'] for d in data]}

	@staticmethod
	def parse_response(response):
		if response.content:
			return json.loads(response.content)


	def make_request(self, end_point, method, data):
		response = self.conn.request(method, end_point, auth=self.conn.auth, json=data, verify=False)
		return self.parse_response(response)


