# third-party imports
from flask_restplus import Resource
from flask_bcrypt import Bcrypt
import jwt

# local imports
from ..models.user import user_class
from ..utils.udto import api, register_parser, login_model, login_parser, register_model
from ..utils.validators import validate_user_data


@api.route("/signup")
class UserRegister(Resource):
    """Registers a new user."""

    # @api.marshal_with(users)
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
        # print(user_class.no_of_users)
        if user:
            return {'message': 'Username or Email exists, please login or register with another email'}, 400
        # check if username exists
        user = user_class.get_user_by_username(new_user["username"])
        if not user:
            # hash_password = Bcrypt().generate_password_hash(new_user["password"]).decode()
            # user_class.create_user(new_user["username"], new_user["email"], hash_password)
            user_class.create_user(new_user)
            # print(new_user)
            # import pdb;pdb.set_trace()
            # print(user_class.no_of_users)
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
                    # print(x)
                    # if not Bcrypt().check_password_hash(x["password"], args["password"]):
                    #     return {"warning": "Invalid password"},400

                    token = user_class.generate_token(x["user_id"])

                    # return {"message": "Logged in successfully"}
                    return {"message": "Logged in successfully", "token": token.decode("UTF-8")}
                    # return {"message": "Logged in successfully", "token": token}

            return {"warning": "No user found. Please sign up"},401
        return {"warning": "'username' and 'password' are required fields"}, 400