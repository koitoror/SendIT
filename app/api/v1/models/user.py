from datetime import datetime, timedelta

# local imports
import jwt
from flask import current_app


class User(object):
    """ CLASS FOR ADDING, EDITING AND DELETING USERS."""

    def __init__(self):
        """constructor method"""
        self.no_of_users = [{
            "user_id": 1,
            "confirm": "johndoe123",
            "email": "johndoe@gmail.com",
            "username": "johndoe",
            "password": "johndoe123",
            "admin": True
        }]

    @staticmethod
    def generate_token(user_id):
        """token generation for authentication"""
        try:
            payload = {"exp": datetime.utcnow() + timedelta(days=1),
                       "iat": datetime.utcnow(),
                       "sub": user_id}
            return jwt.encode(payload, current_app.config.get("SECRET_KEY"))
        except Exception as e:
            return {"message": str(e)}

    @staticmethod
    def generate_token1(user_id, admin):
        """token generation for authentication"""
        try:
            payload = {"exp": datetime.utcnow() + timedelta(days=1),
                       "iat": datetime.utcnow(),
                       "admin": admin,
                       "sub": user_id}
            return jwt.encode(payload, current_app.config.get("SECRET_KEY"))
        except Exception as e:
            return {"message": str(e)}

    def create_user(self, data):
        """Method for creating an user"""
        data["user_id"] = int(len(self.no_of_users) + 1)
        data["date_registered"] = str(
            datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        data['admin'] = False
        self.no_of_users.append(data)
        return data

    def get_user_by_email(self, email):
        """Method for fetching one user by its email"""
        user = [user for user in self.no_of_users if user["email"] == email]
        return user

    def get_user_by_username(self, username):
        """Method for fetching one user by its username"""
        user = [user for user in self.no_of_users
                if user["username"] == username]
        return user


user_class = User()
