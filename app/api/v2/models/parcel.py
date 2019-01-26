from datetime import datetime

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
        cursor.execute(query, (parcel_name, price, pickup_location,
                               destination_location, status, user_id))

    @staticmethod
    def get_parcel_by_id(dict_cursor, parcel_id):
        query_string = "SELECT * FROM parcels WHERE parcel_id=%s"
        dict_cursor.execute(query_string, [parcel_id])
        data = dict_cursor.fetchone()
        if not data:
            api.abort(404, "Parcel {} not found".format(parcel_id))
        parcel = {key: str(value)
                  for key, value in data.items() if value is not str}


        obj = {                                         
            "parcel_id": parcel["parcel_id"],
            "parcel_name": parcel["parcel_name"],
            "pickup_location": parcel["pickup_location"],
            "destination_location": parcel["destination_location"],
            "price": parcel["price"],
            "status": parcel["status"],
            "user_id": parcel["user_id"],
            "date_ordered": datetime.strptime(parcel["date_ordered"], '%Y-%m-%d %H:%M:%S.%f+00:00').strftime('%d-%b-%Y : %H:%M:%S')
        }

        return obj

    @staticmethod
    def modify_parcel_user_cancel(dict_cursor, cursor, status, date_modified, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized to edit this parcel order")
        if data["status"] == "DELIVERED":
            api.abort(401, "Parcel order cannot be canceled since it has been delivered to the destination!")

        query = "UPDATE parcels SET status=%s, date_modified=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (status, date_modified, parcel_id))

    @staticmethod
    def modify_parcel_user_destination(dict_cursor, cursor, destination_location, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized to edit this parcel order")
        query = "UPDATE parcels SET destination_location=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (destination_location, parcel_id))

    @staticmethod
    def modify_parcel_admin_pl(dict_cursor, cursor, present_location, parcel_id):
        query = "UPDATE parcels SET present_location=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (present_location, parcel_id))

    @staticmethod
    def modify_parcel_admin_status(dict_cursor, cursor, status, parcel_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["status"] == "DELIVERED":
            api.abort(401, "Parcel order cannot be canceled since it has been delivered to the destination!")
        query = "UPDATE parcels SET status=%s WHERE (parcel_id=%s)"
        cursor.execute(query, (status, parcel_id))

    @staticmethod
    def delete_parcel(dict_cursor, cursor, parcel_id, user_id):
        data = Parcel.get_parcel_by_id(dict_cursor, parcel_id)
        if data["user_id"] != str(user_id):
            api.abort(401, "Unauthorized to delete this parcel order")
        query = "DELETE FROM parcels WHERE parcel_id=%s"
        dict_cursor.execute(query, [parcel_id])

    @staticmethod
    def get_all_by_user(dict_cursor, user_id):
        query_string = "SELECT * FROM parcels WHERE user_id = %s"
        dict_cursor.execute(query_string, [user_id])
        parcels = dict_cursor.fetchall()
        if not parcels:
            api.abort(404, "No parcels for user {}".format(user_id))
        results = []
        for parcel in parcels:

            obj = {
                "parcel_id": parcel["parcel_id"],
                "parcel_name": parcel["parcel_name"],
                "pickup_location": parcel["pickup_location"],
                "present_location": parcel["present_location"],
                "destination_location": parcel["destination_location"],
                "cancel_order": parcel["cancel_order"],                
                "price": parcel["price"],
                "status": parcel["status"],
                "user_id": parcel["user_id"],
                "date_ordered": parcel["date_ordered"].strftime('%d-%b-%Y : %H:%M:%S'),
            }
            results.append(obj)
        return results

    @staticmethod
    def get_all_by_admin(dict_cursor):
        query_string = "SELECT * FROM parcels"
        dict_cursor.execute(query_string)
        parcels = dict_cursor.fetchall()
        results = []
        for parcel in parcels:
            obj = {
                "parcel_id": parcel["parcel_id"],
                "parcel_name": parcel["parcel_name"],
                "pickup_location": parcel["pickup_location"],
                "present_location": parcel["present_location"],
                "destination_location": parcel["destination_location"],
                "cancel_order": parcel["cancel_order"],                
                "price": parcel["price"],
                "status": parcel["status"],
                "user_id": parcel["user_id"],
                "date_ordered": parcel["date_ordered"].strftime('%d-%b-%Y : %H:%M:%S'),
            }
            results.append(obj)
        return results
