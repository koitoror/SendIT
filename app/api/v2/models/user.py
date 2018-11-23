from datetime import datetime, timedelta

import jwt
from flask import current_app
from flask_bcrypt import Bcrypt


class User():
    """Defines the User model"""
    def __init__(self, user_id, username, email, password, confirm, admin):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = Bcrypt().generate_password_hash(password)
        self.confirm = confirm
        self.admin = admin

    @staticmethod
    def generate_token(user_id, admin):
        """token generation for authentication"""
        try:
            payload = {"exp":datetime.utcnow() + timedelta(days=1),
                       "iat":datetime.utcnow(),
                       "sub":user_id,
                       "admin":admin}
            return jwt.encode(payload, current_app.config.get("SECRET_KEY"))
        except Exception as e:
            return {"message": str(e)}

    @staticmethod
    def create_user(cursor, username, email, password):
        query = "INSERT INTO users (username,email,password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
    
    @staticmethod
    def create_admin(cursor, username, email, password, admin):
        query = "INSERT INTO users (username,email,password,admin) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (username, email, password, admin))
    
    @staticmethod
    def get_user_by_username(dict_cursor, username):
        query_string="SELECT * FROM users WHERE username = %s"
        dict_cursor.execute(query_string, [username])
        user = dict_cursor.fetchone()
        return user

    @staticmethod
    def get_user_by_email(dict_cursor, email):
        query_string="SELECT * FROM users WHERE email = %s"
        dict_cursor.execute(query_string, [email])
        user = dict_cursor.fetchone()
        return user

    # @staticmethod
    # def logout_user(dict_cursor, cursor, self, token):
    #     """logs out a user by adding their token to the blacklist table"""
    #     query_string = "INSERT INTO blacklist VALUES (%(tokens)s) RETURNING tokens"
    #     bad_token = dict(tokens=token)
    #     dict_cursor.execute(query_string, bad_token)
    #     bad_token = dict_cursor.fetchone()[0]
    #     cursor.commit()
    #     dict_cursor.close()
    #     return bad_token
