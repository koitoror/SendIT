"""Contains the user_required decorator to restrict access
to authenticated users only and the admin_required decorator
to restrict access to administrators only.
"""

from functools import wraps
from flask import request, current_app, jsonify, make_response
import jwt

# local imports
from ..utils.udto import api


def user_required(f):
    """Ensures user is logged in before action
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        user_id = ""
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

        return f(user_id, *args, **kwargs)

    return wrap


def admin_required(f):
    """Ensures admin user is logged in before action
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        admin = ""
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            api.abort(400, "Token Missing")
        try:
            payload = jwt.decode(token, current_app.config.get("SECRET_KEY"))
            # user_id = payload['sub']
            if payload['admin'] is not True:
                return make_response(jsonify({
                    "message": "Not authorized to perform this function"}),
                    401)

        except jwt.ExpiredSignatureError:
            api.abort(400, "Token has expired. Please login again")

        except jwt.InvalidTokenError:
            api.abort(400, "Invalid token")

        return f(admin, *args, **kwargs)

    return wrap


def token_required(f):
    """Ensures user is logged in before action
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        user_id = ""
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

        return f(user_id, *args, **kwargs)
    return wrap
