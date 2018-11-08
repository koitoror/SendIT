# third-party imports
from flask_restplus import Resource
from flask import request
from functools import wraps

# local imports
from ..models.user import User as UserClass
from ..models.parcel import Parcel as ParcelClass
from ..utils.pdto import api, parcels, post_parcels, update_parcels_admin, update_parcels_user, parcel_parser, update_parcel_parser_as_admin, update_parcel_parser_as_user
from ..utils.decorators import token_required
from ..utils.validators import validate_parcel_data, validate_update_parcel


parcel = ParcelClass()
user = UserClass()

@api.route("/parcels")
class ParcelList(Resource):
    """Displays a list of all parcels and lets you POST to add new parcel delivery orders."""


    @api.doc("list_parcel_delivery_orders", security='apikey')
    @api.response(404, "Parcel delivery orders Not Found")
    @api.marshal_list_with(parcels, envelope="parcels")
    @token_required
    def get(self):
        """Fetch/list all parcel delivery orders"""
        return parcel.get_all()

