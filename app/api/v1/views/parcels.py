# third-party imports
from flask_restplus import Resource


# local imports
from ..models.parcel import parcel_class
from ..utils.pdto import api, parcel, post_parcels, update_parcels_admin
from ..utils.pdto import parcel_parser, update_parcel_parser_as_admin
from ..utils.pdto import update_parcel_parser_as_user, update_parcels_user
from ..utils.decorators import user_required, admin_required
from ..utils.validators import validate_parcel_data, validate_update_parcel
from ..utils.validators import validate_update_parcel_admin


@api.route("/parcels")
class ParcelList(Resource):
    """Displays a list of all parcels and lets you POST new parcel delivery."""

    @api.expect(post_parcels)
    @api.doc('creates a parcel delivery order', security='apikey')
    @api.response(201, "Created")
    @user_required
    def post(user_id, self):
        """Creates a new Parcel delivery order."""
        args = parcel_parser.parse_args()
        invalid_data = validate_parcel_data(args)
        if invalid_data:
            return invalid_data

        return parcel_class.create_parcel(args, user_id), 201

    @api.doc("list_parcel_delivery_orders", security='apikey')
    @api.response(404, "Parcel delivery orders Not Found")
    @api.marshal_list_with(parcel, envelope="parcels")
    @admin_required
    def get(admin, self):
        """Fetch/list all parcel delivery orders"""
        return parcel_class.get_all(admin=True)


@api.route("/parcels/<int:parcel_id>")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel not found')
class Parcel(Resource):
    """Displays a single parcel item and lets you delete them."""

    @api.marshal_with(parcel)
    @api.doc('get one parcel delivery order', security='apikey')
    @user_required
    def get(self, user_id, parcel_id):
        """Fetch/display a specific/single parcel delivery order."""
        return parcel_class.get_one(parcel_id, user_id)

    @api.marshal_with(parcel)
    @api.doc('updates a parcel delivery order for admin', security='apikey')
    @api.expect(update_parcels_admin)
    @user_required
    def put(self, user_id, parcel_id):
        """Updates a single Parcel delivery order by admin."""
        args = update_parcel_parser_as_admin.parse_args()
        invalid_data = validate_update_parcel_admin(parcel, args)
        if invalid_data:
            return invalid_data
        return parcel_class.update_parcel(parcel_id, user_id, args)

    @api.marshal_with(parcel)
    @api.doc('deletes a parcel delivery order', security='apikey')
    @api.response(204, 'Parcel Deleted')
    @user_required
    def delete(self, user_id, parcel_id):
        """Deletes a single Parcel delivery order."""
        parcel_class.delete_parcel(parcel_id, user_id)
        return '', 204


@api.route("/users/<int:user_id>/parcels")
@api.param("user_id", "parcel identifier")
@api.response(404, 'Parcel not found')
class User(Resource):
    """Displays a single parcel item and lets you delete them."""

    @api.doc("list_all_parcel_delivery_orders_by_user", security='apikey')
    @api.response(404, "Parcel delivery orders Not Found")
    @api.marshal_list_with(parcel, envelope="parcels")
    def get(self, user_id):
        """Fetch/list all parcel delivery orders by a specific/single user"""
        return parcel_class.get_all_by_user(user_id)


@api.route("/parcels/<int:parcel_id>/cancel")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel not found')
class UserParcel(Resource):
    """Displays a single parcel deliver order and lets you cancel order."""

    @api.marshal_with(parcel)
    @api.doc('updates/cancels a parcel delivery order', security='apikey')
    @api.expect(update_parcels_user)
    @user_required
    def put(self, user_id, parcel_id):
        """Cancels a single Parcel delivery order by user."""
        args = update_parcel_parser_as_user.parse_args()
        invalid_data = validate_update_parcel(parcel, args)
        if invalid_data:
            return invalid_data
        return parcel_class.update_parcel(parcel_id, user_id, args)
