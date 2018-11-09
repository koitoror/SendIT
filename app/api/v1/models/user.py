from datetime import datetime, timedelta

# local imports
import jwt
from flask import current_app
from flask_bcrypt import Bcrypt
from ..utils.udto import api


class User(object):
    """ CLASS FOR ADDING, EDITING AND DELETING USERS."""

    def __init__(self):
        """constructor method"""
        # import pdb;pdb.set_trace()
        self.no_of_users = []

    @staticmethod
    def generate_token1(self, user_id):
        """token generation for authentication"""
        try:
            payload = {
                'id': user_id,
                # 'usertype': User.get_one(self, user_id)['usertype'],
                "exp":datetime.utcnow() + timedelta(days=1),
                "iat":datetime.utcnow()
            }
            return jwt.encode(payload, current_app.config.get("SECRET_KEY"))
        except Exception as e:
            return {"message": str(e)}

    @staticmethod
    def generate_token(user_id):
        """token generation for authentication"""
        try:
            payload = {"exp":datetime.utcnow() + timedelta(days=1),
                       "iat":datetime.utcnow(),
                       "sub":user_id}
            return jwt.encode(payload, current_app.config.get("SECRET_KEY"))
        except Exception as e:
            return {"message": str(e)}

    def create_user(self, data):
        """Method for creating an user"""

        data["user_id"] = int(len(self.no_of_users) + 1)
        data["date_registered"] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        # data["usertype"] = "user"
        data['admin'] = False
        self.no_of_users.append(data)
        return data
        # return self.no_of_users

    def get_one(self, user_id):
        """Method for fetching one user by its id"""
        user = [user for user in self.no_of_users if user["user_id"] == user_id]

        if not user:
            api.abort(404, "User {} does not exist".format(user_id))
        return user
    
    def get_user_by_email(self, email):
        """Method for fetching one user by its email"""
        user = [user for user in self.no_of_users if user["email"] == email]
        return user

    def get_user_by_username(self, username):
        """Method for fetching one user by its username"""
        user = [user for user in self.no_of_users if user["username"] == username]
        return user

    def get_user_by_id(self, user_id):
        """Method for fetching one user by its username"""
        user = [user for user in self.no_of_users if user["user_id"] == user_id]
        return user

    # def is_admin(self, user_id):
    #     """Method for fetching one user by its username"""
    #     user = [user for user in self.no_of_users if user["admin"] = True and ]
    #     if not user:
    #         api.abort(401, 'you cannot perform the opertion')
    #     return user

    def get_user_by_password(self, password):
        """Method for fetching one user by its password"""
        user = [user for user in self.no_of_users if user["password"] == password]
        return user

    def delete_user(self, user_id):
        "Method for deleting an user"

        user = self.get_one(user_id)
        self.no_of_users.remove(user[0])

    def update_user(self, user_id, data):
        """Method for updating an user"""

        user = self.get_one(user_id)
        data['date_promoted'] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        # data["usertype"] = "admin"
        user[0].update(data)
        return user

    def promote_user(self, user_id, data):
        """Method for promoting a user to admin"""

        user = self.get_one(user_id)
        data['date_promoted'] = str(datetime.now().strftime('%b-%d-%Y : %H:%M:%S'))
        data["admin"] = True
        user[0].update(data)
        return user

    def get_all(self):
        """Method for returning all users."""
        users = [users for users in self.no_of_users]
        if not users:
            api.abort(404, "No Users Found.")
        return users

user_class = User()