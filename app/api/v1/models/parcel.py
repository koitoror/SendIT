from datetime import datetime
from flask import request, current_app, jsonify, make_response
import jwt

#local imports
from ..utils.pdto import api
from ..utils.validators import validate_parcel_data, validate_update_parcel
from instance import config


class Parcel(object):
    """ CLASS FOR ADDING, EDITING AND DELETING PARCEL DELIVERY ORDERS."""

    def __init__(self):
        """constructor method"""

        self.no_of_parcels = []

    def create_parcel(self, data):
        """Method for creating a parcel delivery order"""

        data["id"] = int(len(self.no_of_parcels) + 1)
        data["date_ordered"] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        
        # token = request.headers['x-access-token']
        # payload = jwt.decode(token, config.Config.SECRET_KEY)
        # data['user_id'] = payload['id']

        self.no_of_parcels.append(data)
        return data


    def get_one(self, parcel_id):
        """Method for fetching one parcel by its id"""
        parcel = [parcel for parcel in self.no_of_parcels if parcel["id"] == parcel_id]

        if not parcel:
            api.abort(404, "Parcel delivery order {} does not exist".format(parcel_id))
        return parcel

    def delete_parcel(self, parcel_id):
        "Method for deleting a parcel"

        parcel = self.get_one(parcel_id)
        self.no_of_parcels.remove(parcel[0])

    def update_parcel(self, parcel_id, data):
        """Method for updating a parcel"""

        parcel = self.get_one(parcel_id)
        data['date_modified'] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        parcel[0].update(data)
        return parcel

    def get_all(self):
        """Method for returning all parcels."""
        parcels = [parcels for parcels in self.no_of_parcels]
        if not parcels:
            api.abort(404, "No Parcel Delivery Orders Found.")
            for x in parcels:
                invalid_data = validate_parcel_data(x)
                if invalid_data:
                    return invalid_data
        return parcels