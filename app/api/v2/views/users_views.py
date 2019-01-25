# third-party imports
from flask_restplus import Resource
from flask_bcrypt import Bcrypt

# local imports
from app.database import Database
from ..models.user import User
from ..utils.udto import api, register_parser, login_parser
from ..utils.udto import register_model, login_model
from ..utils.validators import validate_user_data


# initializing our db connection
conn = Database()
conn.create_tables()
cursor = conn.cursor
dict_cursor = conn.dict_cursor


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
        user = User.get_user_by_email(dict_cursor, new_user['email'])
        if user:
            return {
                'message':
                'Email exists, please login or register with another email'
            }, 400
        invalid_data = validate_user_data(new_user)
        if invalid_data:
            return invalid_data
        # check in the db if user exists
        user = User.get_user_by_username(dict_cursor, new_user["username"])
        if not user:
            hash_password = Bcrypt().generate_password_hash(
                new_user["password"]).decode()
            User.create_user(
                cursor, new_user["username"], new_user["email"], hash_password)
            return {"message": "User registered successfully"}, 201
        return {"warning": "User already exists. Please login."}, 202


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
            user = User.get_user_by_username(dict_cursor, args["username"])
            if user:
                if not Bcrypt().check_password_hash(user["password"],
                                                    args["password"]):
                    return {"warning": "Invalid password"}, 400

                token = User.generate_token(user["id"], user["admin"])

                return {"message": "Logged in successfully",
                        "user_id": user["id"],
                        "admin": user["admin"],
                        "token": token.decode("UTF-8")},
            return {"warning": "No user found. Please sign up"}, 401
        return {"warning": "'username' and 'password' are required fields"},
        400
