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

    @api.expect(post_parcels)
    @api.doc('creates a parcel delivery order', security='apikey')
    @api.response(201, "Created")
    @token_required
    def post(self):
        """Creates a new Parcel delivery order."""
        args = parcel_parser.parse_args()
        invalid_data = validate_parcel_data(args)
        if invalid_data:
            return invalid_data
        return parcel.create_parcel(args),201

    @api.doc("list_parcel_delivery_orders", security='apikey')
    @api.response(404, "Parcel delivery orders Not Found")
    @api.marshal_list_with(parcels, envelope="parcels")
    @token_required
    def get(self):
        """Fetch/list all parcel delivery orders"""
        return parcel.get_all()

@api.route("/parcels/<int:parcelId>")
@api.param("parcelId", "parcel identifier")
@api.response(404, 'Parcel not found')
class Parcel(Resource):
    """Displays a single parcel item and lets you delete them."""

    @api.marshal_with(parcels)
    @api.doc('get one parcel delivery order', security='apikey')
    @token_required
    def get(self, parcelId):
        """Fetch/display a specific/single parcel delivery order."""
        
        return parcel.get_one(parcelId)

    @api.marshal_with(parcels)
    @api.doc('updates a parcel delivery order for admin', security='apikey')
    @api.expect(update_parcels_admin)
    @token_required
    def put(self, parcelId):
        """Updates a single Parcel delivery order by admin."""
        args = update_parcel_parser_as_admin.parse_args()
        invalid_data = validate_update_parcel(parcel, args)
        if invalid_data:
            return invalid_data
        return parcel.update_parcel(parcelId, args)
    
    @api.marshal_with(parcels)
    @api.doc('deletes a parcel delivery order', security='apikey')
    @api.response(204, 'Parcel Deleted')
    @token_required
    def delete(self, parcelId):
        """Deletes a single Parcel delivery order."""
        parcel.delete_parcel(parcelId)
        return '',204

