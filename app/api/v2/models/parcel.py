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

    @staticmethod
    def get_parcel_by_id(dict_cursor, parcel_id):
        query_string="SELECT * FROM parcels WHERE parcel_id=%s"
        dict_cursor.execute(query_string, [parcel_id])
        data = dict_cursor.fetchone()
        if not data:
            api.abort(404, "Parcel {} not found".format(parcel_id))
        parcel = {key:str(value) for key, value in data.items() if value is not str}
        return parcel
     
