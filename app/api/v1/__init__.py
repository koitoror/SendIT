from flask_restplus import Api
from flask import Blueprint

# local imports
from .views.users import api as users_ns
from .views.parcels import api as parcels_ns


api_v1 = Blueprint('api1', __name__)


authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'x-access-token'
    }
}


api = Api(api_v1, title='SendIT API :: v1', doc='/', version='1.0', authorizations=authorizations,
    description='SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.',
)


del api.namespaces[0]
api.add_namespace(users_ns, path='/api/v1/auth')
api.add_namespace(parcels_ns, path='/api/v1')