from flask import jsonify, current_app, request
from app.main import bp
from app.models import StoreDataLoader
from app.main import bp
from app.libs import PostcodesHelper

@bp.route('/stores/', methods=['GET'])
def get_stores():
	search_string = request.args.get('query', '')
	limit = request.args.get('limit', 10, type=int)
	offset = request.args.get('offset', 0, type=int)
	with_coordinates = request.args.get('with_coordinates', '', type=str)
	stores = StoreDataLoader().load_data(search_string, limit, offset)
	if with_coordinates.lower()=='true': ## Python evaluavtes all non-empty strings to true; hence cannot do a bool check
		response = PostcodesHelper().fetch_postcode_details(stores)
		stores = [{**u, **v} for u, v in zip(stores, response)]
	return jsonify(stores)

# Sanity check route
@bp.route('/ping', methods=['GET'])
def ping_pong():
	return jsonify('pong!')