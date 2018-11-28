from flask_restplus import Api
from flask import Blueprint

from .views.users_views import api as auth_ns
from .views.parcels_views import api as parcels_ns


api_v2 = Blueprint('api', __name__)


authorizations = {
    "apikey": {
        "type": "apiKey",
        "in": "header",
        "name": "x-access-token"
    }
}

api = Api(
    api_v2, title='SendIT API :: v2', doc='/', version='2.0',
    authorizations=authorizations,
    description='SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.',
)

del api.namespaces[0]
api.add_namespace(auth_ns, path="/api/v2/auth")
api.add_namespace(parcels_ns, path="/api/v2")
