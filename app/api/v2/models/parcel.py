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

    @staticmethod   
    def modify_parcel(dict_cursor, cursor, parcel_name, status, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "UPDATE parcels SET parcel_name=%s, status=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (parcel_name, status, parcel_id))


    @staticmethod   
    def modify_parcel_user_cancel(dict_cursor, cursor, cancel_order, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "UPDATE parcels SET cancel_order=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (cancel_order, parcel_id))

    @staticmethod   
    def modify_parcel_user_destination(dict_cursor, cursor, destination_location, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "UPDATE parcels SET destination_location=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (destination_location, parcel_id))
    
    @staticmethod   
    def modify_parcel_admin_pl(dict_cursor, cursor, present_location, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "UPDATE parcels SET present_location=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (present_location, parcel_id))

    @staticmethod   
    def modify_parcel_admin_status(dict_cursor, cursor, status, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized")
        query = "UPDATE parcels SET status=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (status, parcel_id))
     

     
