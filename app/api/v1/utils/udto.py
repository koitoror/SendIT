from flask_restplus import Namespace, fields, reqparse


api = Namespace("auth", description="authentication related operations")

user = api.model(
    'user', {
        "user_id": fields.Integer(),
        "date_registered": fields.String(),
        "date_promoted": fields.String(),
        "admin": fields.Boolean(
            required=True, description='user-level', example='False'),
        'email': fields.String(
            required=True, description='email address',
            example='johndoe@gmail.com'),
        'username': fields.String(
            required=True, description='username', example='johndoe'),
        'password': fields.String(
            required=True, description='password', example='johndoe123'),
        'confirm': fields.String(
            required=True, description='password', example='johndoe123')
    })

register_model = api.model(
    'register_user', {
        'email': fields.String(
            required=True, description='email address',
            example='johndoe@gmail.com'),
        'username': fields.String(
            required=True, description='username', example='johndoe'),
        'password': fields.String(
            required=True, description='password', example='johndoe123'),
        'confirm': fields.String(
            required=True, description='password', example='johndoe123')
    })

login_model = api.model(
    'login_user', {
        'username': fields.String(
            required=True, description='username', example='johndoe'),
        'password': fields.String(
            required=True, description='password', example='johndoe123')
    })

register_parser = reqparse.RequestParser()
register_parser.add_argument(
    'username', required=True, help='username should be a string')
register_parser.add_argument(
    'email', required=True, help='email should be a string')
register_parser.add_argument(
    'password', required=True, help='password should be a string')
register_parser.add_argument(
    'confirm', required=True, help='password should be a string')

login_parser = register_parser.copy()
login_parser.remove_argument('email')
login_parser.remove_argument('confirm')

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument(
    'username', required=True, help='username should be a string')
update_user_parser.add_argument(
    'email', required=True, help='email should be a string')
update_user_parser.add_argument(
    'password', required=True, help='password should be a string')
update_user_parser.add_argument(
    'confirm', required=True, help='password should be a string')
update_user_parser.add_argument(
    'usertype', required=True, help='password should be a string')
