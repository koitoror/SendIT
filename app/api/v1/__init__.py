from flask_restplus import Api
from flask import Blueprint

# local imports
from .views.users import api as users_ns
from .views.parcels import api as parcels_ns


api_v1 = Blueprint('api1', __name__)


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-token'
    }
}


api2 = Api(
    api_v1, title='SendIT API :: v1', doc='/v1', version='1.0',
    authorizations=authorizations,
    description='SendIT is a courier service that helps to deliver parcels.',)


del api2.namespaces[0]
api2.add_namespace(users_ns, path='/api/v1/auth')
api2.add_namespace(parcels_ns, path='/api/v1')
