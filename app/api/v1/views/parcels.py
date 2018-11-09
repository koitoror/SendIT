# third-party imports
from flask_restplus import Resource
from flask import request
from functools import wraps

# local imports
from ..models.user import user_class
from ..models.parcel import parcel_class
from ..utils.pdto import api, parcel, post_parcels, update_parcels_admin, update_parcels_user, parcel_parser, update_parcel_parser_as_admin, update_parcel_parser_as_user
from ..utils.decorators import token_required, token_required1
from ..utils.validators import validate_parcel_data, validate_update_parcel



@api.route("/parcels")
class ParcelList(Resource):
    """Displays a list of all parcels and lets you POST to add new parcel delivery orders."""

    @api.expect(post_parcels)
    @api.doc('creates a parcel delivery order', security='apikey')
    @api.response(201, "Created")
    @token_required1
    def post(user_id, self):
        """Creates a new Parcel delivery order."""
        args = parcel_parser.parse_args()
        invalid_data = validate_parcel_data(args)
        if invalid_data:
            return invalid_data
        # print(user_id)
        # user = user_class.no_of_users
        # print(user)

        return parcel_class.create_parcel(args, user_id),201

    @api.doc("list_parcel_delivery_orders", security='apikey')
    @api.response(404, "Parcel delivery orders Not Found")
    @api.marshal_list_with(parcel, envelope="parcels")
    @token_required
    def get(self):
        """Fetch/list all parcel delivery orders"""

        return parcel_class.get_all()

@api.route("/parcels/<int:parcel_id>")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel not found')
class Parcel(Resource):
    """Displays a single parcel item and lets you delete them."""

    @api.marshal_with(parcel)
    @api.doc('get one parcel delivery order', security='apikey')
    @token_required
    def get(self, parcel_id):
        """Fetch/display a specific/single parcel delivery order."""
        # print(parcel_id)
        return parcel_class.get_one(parcel_id)

    @api.marshal_with(parcel)
    @api.doc('updates a parcel delivery order for admin', security='apikey')
    @api.expect(update_parcels_admin)
    @token_required
    def put(self, parcel_id):
        """Updates a single Parcel delivery order by admin."""
        args = update_parcel_parser_as_admin.parse_args()
        # invalid_data = validate_update_parcel(parcel_class, args)
        # if invalid_data:
        #     return invalid_data
        return parcel_class.update_parcel(parcel_id, args)
    
    @api.marshal_with(parcel)
    @api.doc('deletes a parcel delivery order', security='apikey')
    @api.response(204, 'Parcel Deleted')
    @token_required
    def delete(self, parcel_id):
        """Deletes a single Parcel delivery order."""
        parcel_class.delete_parcel(parcel_id)
        return '',204


@api.route("/users/<int:user_id>/parcels")
@api.param("user_id", "parcel identifier")
@api.response(404, 'Parcel not found')
class User(Resource):
    """Displays a single parcel item and lets you delete them."""
    
    @api.doc("list_all_parcel_delivery_orders_by_user", security='apikey')
    @api.response(404, "Parcel delivery orders Not Found")
    @api.marshal_list_with(parcel, envelope="parcels")
    @token_required
    def get(self, user_id):
        """Fetch/list all parcel delivery orders by a specific/single user"""
        # print(user_id)
        return parcel_class.get_all_by_user(user_id)
        # return parcel_class.get_all()

@api.route("/parcels/<int:parcel_id>/cancel")
@api.param("parce", "parcel identifier")
@api.response(404, 'Parcel not found')
class UserParcel(Resource):
    """Displays a single parcel parcel deliver order and lets you cancel the order."""

    @api.marshal_with(parcel)
    @api.doc('updates/cancels a parcel delivery order by user', security='apikey')
    @api.expect(update_parcels_user)
    @token_required
    def put(self, parcel_id):
        """Cancels a single Parcel delivery order by user."""
        args = update_parcel_parser_as_user.parse_args()
        # invalid_data = validate_update_parcel(parcel, args)
        # if invalid_data:
        #     return invalid_data
        return parcel_class.update_parcel(args, parcel_id)