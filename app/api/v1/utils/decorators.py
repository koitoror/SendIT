"""Contains the token_required decorator to restrict access to authenticated users only and
the admin_required decorator to restrict access to administrators only.
"""

from functools import wraps

from flask import request, current_app, jsonify, make_response
import jwt

#local imports
from ..utils.udto import api
from instance import config


def token_required(f):
    """Ensures user is logged in before action
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        # user_id = ""
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            api.abort(400, "Token Missing")
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))
            user_id = payload['sub']

        except jwt.ExpiredSignatureError:
            api.abort(400, "Token has expired. Please login again")

        except jwt.InvalidTokenError:
            api.abort(400, "Invalid token")

        return f(*args, **kwargs)
        # return f(user_id, *args, **kwargs)

    return wrap


def token_required1(f):
    """Ensures user is logged in before action
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        # user_id = ""
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            api.abort(400, "Token Missing")
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))
            user_id = payload['sub']

        except jwt.ExpiredSignatureError:
            api.abort(400, "Token has expired. Please login again")

        except jwt.InvalidTokenError:
            api.abort(400, "Invalid token")

        # return f(*args, **kwargs)
        return f(user_id, *args, **kwargs)

    return wrap


def user_required(f):
    """Checks for authenticated users with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        try:
            data = jwt.decode(token, config.Config.SECRET_KEY) # pylint: disable=W0612
        except:
            return make_response(jsonify({
                "message" : "kindly provide a valid token in the header"}), 401)

        return f(*args, **kwargs)

    return decorated

def admin_required(f):
    """Checks for authenticated admins with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """validate token provided and ensures the user is an admin"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        try:
            data = jwt.decode(token, config.Config.SECRET_KEY)
            if data['usertype'] != "admin":
                return make_response(jsonify({
                    "message" : "Not authorized to perform this function as a non-admin"}), 401)

        except:
            return make_response(jsonify({
                "message" : "kindly provide a valid token in the header"}), 401)

        return f(*args, **kwargs)

    return decorated


