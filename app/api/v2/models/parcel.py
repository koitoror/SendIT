from ..utils.pdto import api

class Parcel(object):
    """Defines the Parcel model"""
    def __init__(self, parcel_id, price, pickup_location, destination_location, parcel_name, status, user_id):
        self.parcel_id = parcel_id
        self.price = price
        self.parcel_name = parcel_name
        self.pickup_location = pickup_location
        self.destination_location = destination_location
        self.status = status
        self.created_by = user_id
    
    @staticmethod
    def create_parcel(cursor, parcel_name, price, pickup_location, destination_location, status, user_id):
        query = "INSERT INTO parcels (parcel_name, price, pickup_location, destination_location, status, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (parcel_name, price, pickup_location, destination_location, status, user_id))
