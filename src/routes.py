from flask import request, Response, json, Blueprint
from src.services.suggest_service import SuggestionsService

suggestions = Blueprint('suggestions', __name__)


# GET /suggestions
@suggestions.route('/suggestions', methods=['GET'])
def get_suggestions():
    # Get the query parameter
    q = request.args.get('q')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    # If the query parameter is not provided, return a 400 Bad Request
    if not q:
        return Response(response=json.dumps({'error': 'q parameter is required'}),
                        status=400,
                        mimetype='application/json')
    # If the query parameter is provided, return a 200 OK with a JSON response

    suggest_service = SuggestionsService(latitude, longitude)
    suggested_cities = suggest_service.get_suggestions(q)

    return Response(response=json.dumps({'suggestions': suggested_cities}),
                    status=200,
                    mimetype='application/json')
