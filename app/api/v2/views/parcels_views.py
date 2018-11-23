# third-party imports
from flask_restplus import Resource
from flask_mail import Message, Mail
mail = Mail()


# local imports
from ..models.parcel import Parcel
from ..utils.pdto import api, parcel, post_parcel, parcel_parser, update_parcel_parser, update_parcels_admin_pl, update_parcels_admin_status
from ..utils.pdto import update_parcels_admin, update_parcel_parsers_admin, update_parcel_parser_user_destination
from ..utils.pdto import update_parcels_user, update_parcel_parser_user_cancel, update_parcel_parsers_admin_pl, update_parcel_parsers_admin_status
from ..utils.decorators import token_required, user_required, admin_required
from ..utils.validators import validate_parcel_data, validate_update_parcel, validate_update_parcel_admin_pl
from ..utils.validators import validate_update_parcel_admin, validate_update_parcel_user_destination, validate_update_parcel_admin_status
from app.database import Database

conn = Database()
cursor = conn.cursor
dict_cursor = conn.dict_cursor

@api.route("/parcels")
class ParcelList(Resource):
    """Displays a list of all parcels and lets you POST to add new parcels."""

    @api.expect(post_parcel)
    @api.doc('creates a parcel delivery order', security='apikey')
    @api.response(201, "Created")
    @api.header('x-access-token', type=str, description='access token')
    @user_required
    def post(user_id, self):
        """Creates a new Parcel delivery order."""
        args = parcel_parser.parse_args()

        # validate the parcel payload
        invalid_data = validate_parcel_data(args)
        if invalid_data:
            return invalid_data

        parcel_name = args["parcel_name"]
        status = args["status"]
        pickup_location = args["pickup_location"]
        destination_location = args["destination_location"]
        price = args["price"]
        Parcel.create_parcel(cursor, parcel_name, price, pickup_location, destination_location, status, user_id)
        return {"message": "Parcel added successfully"}, 201

    @api.doc("list_parcels", security='apikey')
    @api.response(404, "Parcels Not Found")
    @api.response(401, "Unauthorized to view these parcels")
    @api.header('x-access-token', type=str, description='access token')
    @admin_required
    def get(self):
        """List all Parcels"""

        parcels = Parcel.get_all_admin(dict_cursor)
        if not parcels:
            api.abort(404, "No all parcels for all user to view by admin")
        return parcels

@api.response(401, "Unauthorized to view this parcel")
@api.route("/parcels/<int:parcel_id>")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class ParcelClass(Resource):
    """Displays a single parcel item and lets you delete them."""

    @api.marshal_with(parcel)
    @api.doc('get one parcel')
    @user_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def get(user_id, self, parcel_id):
        """Displays a single Parcel."""
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if parcel["user_id"] != str(user_id):
            api.abort(401, "Unauthorized to view this parcel")
        return parcel

    @api.doc('updates a parcel', security='apikey')
    @api.expect(post_parcel)
    @api.response(401, "Unauthorized to edit this parcel")
    @user_required
    @api.header('x-access-token', type=str, description='access token')
    def put(user_id, self, parcel_id):
        """Updates a single Parcel."""
        args = update_parcel_parser.parse_args()
        parcel_name = args["parcel_name"]
        status = args["status"]
        parcel = {"parcel_name": parcel_name, "status":status}
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)

        invalid_data = validate_update_parcel(parcel, args)

        if invalid_data:
            return invalid_data
        
        Parcel.modify_parcel(dict_cursor, cursor, args["parcel_name"], args["status"], parcel_id, user_id)
        return {"message": "Updated successfully", "parcel":parcel}

    @api.doc('deletes a parcel')
    @api.response(204, 'Parcel Deleted')
    @user_required
    @api.response(401, "Unauthorized to edit this parcel")
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def delete(user_id, self, parcel_id):
        """Deletes a single Parcel."""

        Parcel.delete_parcel(dict_cursor, cursor, parcel_id, user_id)
        return {"message": "Parcel deleted successully"}, 200

@api.route("/users/<int:user_id>/parcels")
@api.param("user_id", "user identifier")
@api.response(404, 'Parcel order not found')
class UserParcels(Resource):
    """Displays a single parcel item and lets you delete them."""

    @api.doc("list_all_parcel_delivery_orders_by_user", security='apikey')
    @api.response(404, "Parcel delivery orders Not Found")
    @api.response(401, "Unauthorized to view these parcels")
    @token_required
    @api.header('x-access-token', type=str, description='access token')
    def get(self, user_id):


        """Fetch/list all parcel delivery orders by a specific/single user"""
        parcels = Parcel.get_all(dict_cursor, user_id)

        for parcel in parcels:
            # if parcel["user_id"] != int(user_id):
            if str(user_id) == parcel["user_id"]:
                api.abort(401, "Unauthorized to view this parcel")
            elif str(user_id) != parcel["user_id"]:
                # return parcels  
                # return {"message": "Unauthorized to view this parcel"}, 401
                if not parcels:
                    api.abort(404, "No parcels for user {}".format(user_id))
                    # api.abort(401, "Unauthorized to view this parcel")

        return parcels

@api.route("/parcels/<int:parcel_id>/cancel")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class UserCancel(Resource):
    """Displays a single parcel deliver order and lets you cancel order."""

    @api.doc('updates/cancels a parcel delivery order', security='apikey')
    @api.expect(update_parcel_parser_user_cancel)
    @user_required
    @api.response(401, "Unauthorized to edit this parcel")
    @api.header('x-access-token', type=str, description='access token')
    def put(user_id, self, parcel_id):
        """Cancels a single Parcel delivery order by user."""

        args = update_parcel_parser_user_cancel.parse_args()

        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)


        Parcel.modify_parcel_user_cancel(dict_cursor, cursor, args["cancel_order"], parcel_id, user_id)
        return {"message": "Order canceled successfully", "parcel":parcel}

         
@api.route("/parcels/<int:parcel_id>/destination")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class UserDestination(Resource):
    """Displays a single parcel deliver order and lets you cancel order."""

    @api.doc('updates destination of a parcel delivery order', security='apikey')
    @api.expect(update_parcel_parser_user_destination)
    @user_required
    @api.response(401, "Unauthorized to edit this parcel")
    @api.header('x-access-token', type=str, description='access token')
    def put(user_id, self, parcel_id):
        """Changes the destination of a single Parcel delivery order by user."""

        args = update_parcel_parser_user_destination.parse_args()
        destination_location = args["destination_location"]
        parcel = {"destination_location": destination_location}
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        
        invalid_data = validate_update_parcel_user_destination(parcel, args)
        
        if invalid_data:
            return invalid_data

        Parcel.modify_parcel_user_destination(dict_cursor, cursor, args["destination_location"], parcel_id, user_id)
        return {"message": "Destination updated successfully", "parcel":parcel}

@api.route("/parcels/<int:parcel_id>/presentLocation")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class AdminPresentLocation(Resource):
    """Displays a single parcel deliver order and lets you/admin to change the present location."""

    @api.doc('updates present location of a parcel delivery order', security='apikey')
    @api.expect(update_parcel_parsers_admin_pl)
    @admin_required
    @api.response(401, "Unauthorized to edit this parcel")
    @api.header('x-access-token', type=str, description='access token')
    def put(self, parcel_id):
        """Changes the present location of a single Parcel delivery order by admin."""

        args = update_parcel_parsers_admin_pl.parse_args()
        present_location = args["present_location"]
        parcel = {"present_location": present_location}
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        
        invalid_data = validate_update_parcel_admin_pl(parcel, args)
        
        if invalid_data:
            return invalid_data

        Parcel.modify_parcel_admin_pl(dict_cursor, cursor, args["present_location"], parcel_id)

        # msg = Message("Parcel Order !!! Present Location Changed",
        #           sender="dan@send-it-ke.com",
        #         #   recipients=args["email"])
        #           recipients=["recipient@example.com"])
        # mail.send(msg)

        return {"message": "Present location updated successfully", "parcel":parcel}

@api.route("/parcels/<int:parcel_id>/status")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class AdminStatus(Resource):
    """Displays a single parcel deliver order and lets you/admin to change the status."""

    @api.doc('updates status of a parcel delivery order', security='apikey')
    @api.expect(update_parcel_parsers_admin_status)
    @admin_required
    @api.response(401, "Unauthorized to edit this parcel")
    @api.header('x-access-token', type=str, description='access token')
    def put(self, parcel_id):
        """Changes the status of a single Parcel delivery order by admin."""

        args = update_parcel_parsers_admin_status.parse_args()
        status = args["status"]
        parcel = {"status": status}
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        
        invalid_data = validate_update_parcel_admin_status(parcel, args)
        if invalid_data:
            return invalid_data

        Parcel.modify_parcel_admin_status(dict_cursor, cursor, args["status"], parcel_id)
        return {"message": "Status updated successfully", "parcel":parcel}
        