# third-party imports
from flask_restplus import Resource
from flask_bcrypt import Bcrypt


# local imports
from ..models.user import user_class
from ..utils.udto import api, register_parser, login_model
from ..utils.udto import login_parser, register_model

from ..utils.validators import validate_user_data


@api.route("/signup")
class UserRegister(Resource):
    """Registers a new user."""
    @api.expect(register_model)
    @api.doc("user registration")
    @api.response(201, "Created")
    @api.response(400, "Bad Request")
    def post(self):
        """handles registering a user """
        new_user = register_parser.parse_args()
        invalid_data = validate_user_data(new_user)
        if invalid_data:
            return invalid_data
        # check if email exists
        user = user_class.get_user_by_email(new_user['email'])
        if user:
            return {
                'message':
                'Email exists, please login or register with another email'
            }, 400
        # check if username exists
        user = user_class.get_user_by_username(new_user["username"])
        if not user:
            hash_password = Bcrypt().generate_password_hash(
                new_user["password"]).decode()
            
            new_user1 = {
            "password": hash_password,
            "email": new_user["email"],
            "username": new_user["username"]
            }

            user_class.create_user(new_user1)
            
            return {"message": "User registered successfully"}, 201
        return {"message": "User already exists. Please login."}, 202


@api.route("/login")
class LoginUser(Resource):
    "Class for logging in a user"

    @api.expect(login_model)
    @api.doc("user login")
    @api.response(400, "Bad Request")
    @api.response(401, "Unauthorized")
    def post(self):
        "Handles logging the user."
        args = login_parser.parse_args()

        if args["username"] and args["password"]:
            user = user_class.get_user_by_username(args["username"])

            if user:


                for x in user:
                    if not Bcrypt().check_password_hash(x["password"],
                                                        args["password"]):
                        return {"warning": "Invalid password"}, 400

                    token = user_class.generate_token1(
                        x["user_id"], x["admin"])
                    return {"message": "Logged in successfully",
                            "token": token.decode("UTF-8")}

            return {"warning": "No user found. Please sign up"}, 401
        return {"warning": "'username' and 'password' are required fields"},
        400
