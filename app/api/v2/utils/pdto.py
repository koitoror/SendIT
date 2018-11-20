from flask_restplus import Namespace, fields, reqparse


api = Namespace("parcels", description="parcels related operations")

parcel = api.model(
    "parcels", {
        "parcel_id": fields.Integer(),
        "user_id": fields.Integer(),
        "date_ordered": fields.String(),
        "date_modified": fields.String(),
        "parcel_name": fields.String(
            required=True, description="The parcel name",
            example="TRAVEL BAG"),
        "price": fields.Integer(
            required=True, description="The parcel price",
            example=100),
        "present_location": fields.String(
            required=True, description="The parcel present_location",
            example="CITY OFFICE"),
        "pickup_location": fields.String(
            required=True, description="The parcel pickup_location",
            example="DROP VAN"),
        "destination_location": fields.String(
            required=True, description="The parcel destination_location",
            example="MOMBASA"),
        "status": fields.String(
            required=True, description="The parcel status",
            example="UNDELIVERED"),
        "cancel_order": fields.Boolean(
            required=True, description="The parcel cancel delivery order",
            example=False)
    
    })

post_parcel = api.model(
    "post_parcel", {
        "parcel_name": fields.String(
            "parcels name", example="TRAVEL BAG"),
        "price": fields.Integer(
            "parcels price", example=1000),
        "pickup_location": fields.String(
            "parcels pickup_location", example="DROP VAN"),
        "destination_location": fields.String(
            "parcels destination_location", example="MOMBASA"),
        "status": fields.String(
            "parcels status", example="IN TRANSIT"),

    })

update_parcels_admin = api.model(
    "update_parcels_admin", {
        "present_location": fields.String(
            "parcels present_location", example="DISPATCH CENTRE"),
        "status": fields.String(
            "parcels status", example="IN TRANSIT")

    })

update_parcels_admin_pl = api.model(
    "update_parcels_admin", {
        "present_location": fields.String(
            "parcels present_location", example="DISPATCH CENTRE")

    })

update_parcels_admin_status = api.model(
    "update_parcels_admin", {
        "status": fields.String(
            "parcels status", example="IN TRANSIT")

    })

update_parcels_user = api.model(
    "update_parcels_user", {
        "cancel_order": fields.Boolean(
            "parcels cancel_order", example=True),
        "destination_location": fields.String(
            "parcels destination_location", example="MOMBASA")

    })

update_parcels_user_cancel = api.model(
    "update_parcels_user_cancel", {
        "cancel_order": fields.Boolean(
            "parcels cancel_order", example=True)

    })

update_parcels_user_destination = api.model(
    "update_parcels_user_destination", {
        "destination_location": fields.String(
            "parcels destination_location", example="MOMBASA")

    })

parcel_parser = reqparse.RequestParser()
parcel_parser.add_argument(
    'parcel_name', required=True, type=str, help='name should be a string')
parcel_parser.add_argument('price', required=True,
                           type=int,
                           help='price should be a integer')
parcel_parser.add_argument(
    'pickup_location', required=True,
                           type=str,
                           help='pickup_location should be a string')
parcel_parser.add_argument(
    'destination_location', required=True,
                           type=str,
                           help='destination_location should be a string')
parcel_parser.add_argument(
    'status', required=False,
                           type=str,
                           help='status should be a string')

update_parcel_parsers_admin = reqparse.RequestParser()
update_parcel_parsers_admin.add_argument(
    'present_location', type=str,
                        help='present_location should be a string')
update_parcel_parsers_admin.add_argument(
    'status', type=str, help='status should be a string')

update_parcel_parsers_admin_pl = reqparse.RequestParser()
update_parcel_parsers_admin_pl.add_argument(
    'present_location', type=str,
                        help='present_location should be a string')

update_parcel_parsers_admin_status = reqparse.RequestParser()
update_parcel_parsers_admin_status.add_argument(
    'status', type=str, help='status should be a string')

update_parcel_parser_user_destination = reqparse.RequestParser()
update_parcel_parser_user_destination.add_argument(
    'destination_location', type=str,
                            help='destination_location should be a string')

update_parcel_parser_user_cancel = reqparse.RequestParser()
update_parcel_parser_user_cancel.add_argument(
    'cancel_order', type=bool, help='status should be a boolean')

update_parcel_parser = reqparse.RequestParser()
update_parcel_parser.add_argument('parcel_name', required=True, type=str, help='parcel_name should be a string')
update_parcel_parser.add_argument('status', required=True, type=str, help='status should be a string')