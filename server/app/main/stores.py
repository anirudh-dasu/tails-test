from flask import jsonify, current_app, request
from app.main import bp
from app.models import StoreDataLoader
from app.main import bp

@bp.route('/stores', methods=['GET'])
def get_stores():
	search_string = request.args.get('query', '')
	limit = request.args.get('limit', 10, type=int)
	offset = request.args.get('offset', 0, type=int)
	stores = StoreDataLoader().load_data(search_string, limit, offset)
	current_app.logger.info(stores)
	return jsonify(stores)

# Sanity check route
@bp.route('/ping', methods=['GET'])
def ping_pong():
	return jsonify('pong!')