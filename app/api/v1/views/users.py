# third-party imports
from flask_restplus import Resource
from flask_bcrypt import Bcrypt
import jwt

# local imports
from ..models.user import User as UserClass
from ..utils.udto import api, register_parser, login_model, login_parser, register_model
from ..utils.validators import validate_user_data


users = UserClass()

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
        user = users.get_user_by_email(new_user['email'])
        if user:
            return {'message': 'Username or Email exists, please login or register with another email'}, 400
        # check if username exists
        user = users.get_user_by_username(new_user["username"])
        if not user:
            # hash_password = Bcrypt().generate_password_hash(new_user["password"]).decode()
            # users.create_user(new_user["username"], new_user["email"], hash_password)
            users.create_user(new_user)
            return {"message": "User registered successfully"}, 201
        return {"message": "User already exists. Please login."}, 202

