import unittest
import json
import os
from config import Config
from app.models import StoreDataLoader

from app import create_app

class TestConfig(Config):
	TESTING = True

class StoresTest(unittest.TestCase):

	def setUp(self):
		self.app = create_app(TestConfig)
		self.app_context = self.app.app_context()
		self.app_context.push()

	def tearDown(self):
		self.app_context.pop()

	def test_filtering(self):
		store_1 = {'name': 'Orpington', 'postcode': 'BR5 3RP'}
		store_2 = {'name': 'Broadstairs', 'postcode': 'CT10 2RQ'}
		store_3 = {'name': 'Havant', 'postcode': 'PO9 1ND'}

		stores_list = [store_1, store_2, store_3]
		search_string = 'Br'

		response = StoreDataLoader().filter(stores_list, search_string)
		self.assertEqual([store_1, store_2], response)

		search_string = 'AAA'
		response = StoreDataLoader().filter(stores_list, search_string)
		self.assertEqual([], response)

	def test_file_reading(self):
		file_name = os.path.join(os.path.dirname(__file__), 'test.json')
		data = StoreDataLoader().read_file(file_name)

		test_data = [{'name': 'St_Albans', 'postcode': 'AL1 2RJ'}, {'name': 'Hatfield', 'postcode': 'AL9 5JP'}]

		self.assertEqual(data, test_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)