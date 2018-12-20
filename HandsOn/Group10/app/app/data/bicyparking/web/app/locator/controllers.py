# Import flask dependencies
from flask import Blueprint, g, session, request, render_template, make_response
from json import dumps

# Import the database object from the main app module
from app import db, app

# Import module models (i.e. User)
from app.locator.models import BicyPoint

# Define the blueprint: 'auth', set its url prefix: app.url/auth
locator = Blueprint('locator', __name__, url_prefix='/locator')


# Set the route and accepted methods
@locator.route('/', methods=['GET'])
def index():
    return render_template("locator/index.html",)


@locator.route('/stations', methods=['GET'])
def list_stations():
    stations = []
    results = BicyPoint.query.all()
    for result in results:
        stations.append({'id': result.id, 'address': result.address, 'pos': {'lat': result.lat, 'lng': result.lng}})
    response = make_response(dumps(stations))
    response.status_code = 200
    return response

