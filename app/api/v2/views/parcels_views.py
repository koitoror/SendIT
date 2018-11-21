# third-party imports
from flask_restplus import Resource


# local imports
from ..models.parcel import Parcel
from ..utils.pdto import api, parcel, post_parcel, parcel_parser, update_parcel_parser, update_parcels_admin_pl, update_parcels_admin_status
from ..utils.pdto import update_parcels_admin, update_parcel_parsers_admin, update_parcel_parser_user_destination
from ..utils.pdto import update_parcels_user, update_parcel_parser_user_cancel, update_parcel_parsers_admin_pl, update_parcel_parsers_admin_status
from ..utils.decorators import token_required, user_required, admin_required
from ..utils.validators import validate_parcel_data, validate_update_parcel, validate_update_parcel_user_cancel, validate_update_parcel_admin_pl
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
    @user_required
    @api.header('x-access-token', type=str, description='access token')
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
