# third-party imports
from flask_restplus import Resource
from flask_mail import Message, Mail
mail = Mail()
from datetime import datetime

import os
# from flask import current_app

# local imports
from ..models.parcel import Parcel
from ..utils.pdto import api, parcel, post_parcel
from ..utils.pdto import parcel_parser
from ..utils.pdto import update_parcels_user_cancel
from ..utils.pdto import update_parcels_user_destination
from ..utils.pdto import update_parcels_admin_pl, update_parcels_admin_status
from ..utils.pdto import update_parcel_parser_user_destination
from ..utils.pdto import update_parcel_parser_user_cancel
from ..utils.pdto import update_parcel_parsers_admin_pl
from ..utils.pdto import update_parcel_parsers_admin_status
from ..utils.decorators import user_required, admin_required
from ..utils.validators import validate_parcel_data
from ..utils.validators import validate_update_parcel_user_cancel
from ..utils.validators import validate_update_parcel_user_destination
from ..utils.validators import validate_update_parcel_admin_pl
from ..utils.validators import validate_update_parcel_admin_status
from ..models.user import User

from app.database import Database

conn = Database()
cursor = conn.cursor
dict_cursor = conn.dict_cursor


@api.route("/parcels")
class ParcelList(Resource):
    """Displays a list of all parcels and lets you POST to add new parcels."""

    @api.expect(post_parcel)
    @api.doc('creates a parcel delivery order', security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    @api.response(201, "Created")
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
        Parcel.create_parcel(cursor, parcel_name, price,
                             pickup_location, destination_location,
                             status, user_id)
        return {"message": "Parcel added successfully"}, 201

    @api.doc("list_parcels", security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    # @api.marshal_with(parcel, envelope="parcels")
    @api.response(404, "Parcels Not Found")
    @api.response(401, "Unauthorized to view these parcels")
    @admin_required
    def get(self):
        """List all Parcels"""

        parcels = Parcel.get_all_by_admin(dict_cursor)
        if not parcels:
            api.abort(404, "No all parcels for all user to view by admin")
        return parcels


@api.route("/parcels/<int:parcel_id>")
@api.param("parcel_id", "parcel identifier")
@api.response(401, "Unauthorized to view this parcel")
@api.response(404, 'Parcel order not found')
class ParcelClass(Resource):
    """Displays a single parcel item and lets you delete them."""

    @api.doc('get one parcel', security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    # @api.marshal_with(parcel)
    @user_required
    def get(user_id, self, parcel_id):
        """Displays a single Parcel."""
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if parcel["user_id"] != str(user_id):
            api.abort(401, "Unauthorized to view this parcel")
        return parcel

    @api.doc('deletes a parcel', security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    @api.response(204, 'Parcel Deleted')
    @api.response(401, "Unauthorized to delete this parcel")
    @user_required
    def delete(user_id, self, parcel_id):
        """Deletes a single Parcel."""

        Parcel.delete_parcel(dict_cursor, cursor, parcel_id, user_id)
        return {"message": "Parcel deleted successully"}, 200


@api.route("/users/<int:id>/parcels")
@api.param("id", "user identifier")
@api.response(404, 'Parcel order not found')
class UserParcels(Resource):
    """Displays a single parcel item by user."""

    @api.doc("list_all_parcel_delivery_orders_by_user", security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    @api.response(404, "Parcel delivery orders Not Found for user")
    @api.response(401, "Unauthorized to view these parcels")
    @user_required
    def get(user_id, self, id):
        """Fetch/list all parcel delivery orders by a specific/single user"""
        user = User.get_user_by_id(dict_cursor, id)

        if user["id"] != user_id:
            api.abort(401, "Unauthorized to view this parcel")

        parcels = Parcel.get_all_by_user(dict_cursor, user_id)

        return parcels

@api.route("/parcels/<int:parcel_id>/cancel")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class UserCancel(Resource):
    """Displays a single parcel deliver order and lets you cancel order."""

    @api.expect(update_parcels_user_cancel)
    @api.doc('updates/cancels a parcel delivery order', security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    @api.response(401, "Unauthorized to edit/cancel this parcel")
    @user_required
    def put(user_id, self, parcel_id):
        """Cancels a single Parcel delivery order by user."""

        args = update_parcel_parser_user_cancel.parse_args()
        status = args["status"]
        date_modified = str(
            datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        parcel = {"status": status, "date_modified": date_modified}

        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)

        invalid_data = validate_update_parcel_user_cancel(parcel, args)
        if invalid_data:
            return invalid_data

        Parcel.modify_parcel_user_cancel(
            dict_cursor, cursor, args["status"],
            date_modified, parcel_id, user_id)
        return {"message": "Order canceled successfully"}

        # return {"message": "Order canceled successfully", "parcel": parcel}
       


@api.route("/parcels/<int:parcel_id>/destination")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class UserDestination(Resource):
    """Displays a parcel deliver order and lets you change the destination."""

    @api.expect(update_parcels_user_destination)
    @api.doc('updates destination of a parcel delivery order',
             security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    @api.response(401, "Unauthorized to edit this parcel")
    @user_required
    def put(user_id, self, parcel_id):
        """Changes the destination of a Parcel delivery order by user."""

        args = update_parcel_parser_user_destination.parse_args()
        destination_location = args["destination_location"]
        parcel = {"destination_location": destination_location}
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)

        invalid_data = validate_update_parcel_user_destination(parcel, args)

        if invalid_data:
            return invalid_data

        Parcel.modify_parcel_user_destination(
            dict_cursor, cursor, args["destination_location"],
            parcel_id, user_id)
        return {"message": "Destination updated successfully"}

        # return {"message": "Destination updated successfully",
        #         "parcel": parcel}

@api.route("/parcels/<int:parcel_id>/presentLocation")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class AdminPresentLocation(Resource):
    """Displays parcel deliver order and lets admin change present location."""

    @api.expect(update_parcels_admin_pl)
    @api.doc('updates present location of a parcel delivery order',
             security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    @api.response(401, "Unauthorized to edit this parcel")
    @admin_required
    def put(self, parcel_id):
        """Changes the present location of a Parcel delivery order by admin."""

        args = update_parcel_parsers_admin_pl.parse_args()

        present_location = args["present_location"]

        parcel = {"present_location": present_location}

        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        user_id = parcel["user_id"]

        invalid_data = validate_update_parcel_admin_pl(parcel, args)

        if invalid_data:
            return invalid_data

        Parcel.modify_parcel_admin_pl(
            dict_cursor, cursor, present_location, parcel_id)

        user_email = User.get_user_email(dict_cursor, user_id)
        email = user_email[0]
        # print(email)
        msg = Message("Parcel Order !!! Present Location Changed",
              sender = os.getenv("MAIL_USERNAME"),
                # sender = current_app.config.get("MAIL_USERNAME"),
                # subject='SendIT Notification',
                # body='Present Location Changed. Log in to track your parcel. Thanks for choosing SendIT to deliver your parcel',
                # recipients = email)
                # with app.open_resource("static/images/image.jpg") as fp:
                #     msg.attach("images.jpg", "image/jpg", fp.read())
              recipients = ["email"])
        mail.send(msg)

        return {"message": "Present location updated successfully and email notification sent"}

        # return {"message": "Present location updated successfully and notification sent",
        # "parcel": parcel}


@api.route("/parcels/<int:parcel_id>/status")
@api.param("parcel_id", "parcel identifier")
@api.response(404, 'Parcel order not found')
class AdminStatus(Resource):
    """Displays a single parcel deliver order and lets admin change status."""

    @api.expect(update_parcels_admin_status)
    @api.doc('updates status of a parcel delivery order', security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    @api.response(401, "Unauthorized to edit this parcel")
    @admin_required
    def put(self, parcel_id):
        """Changes the status of a single Parcel delivery order by admin."""

        args = update_parcel_parsers_admin_status.parse_args()
        status = args["status"]
        parcel = {"status": status}
        parcel = Parcel.get_parcel_by_id(dict_cursor, parcel_id)

        invalid_data = validate_update_parcel_admin_status(parcel, args)
        if invalid_data:
            return invalid_data

        Parcel.modify_parcel_admin_status(
            dict_cursor, cursor, args["status"], parcel_id)
        return {"message": "Status updated successfully"}
        
        # return {"message": "Status updated successfully", "parcel": parcel}

