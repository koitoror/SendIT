import json
from flask_bcrypt import Bcrypt


from app.api.v2.models.user import User
from app.database import Database
db = Database()
cursor = db.cursor

def register_user(self):
    """helper function for registering a user."""
    return self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='kamardaniel@gmail.com',
            username='kamar',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
def register_admin(self):
    """helper function for registering a user."""
    username='kamar',
    email='kamardaniel@gmail.com',
    password='password123',
    hash_password = Bcrypt().generate_password_hash(password).decode()
    admin = True
    User.create_admin(cursor, username=username, email=email, password=hash_password, admin=admin)
    pass

def login_user(self):
    """helper function for login a user."""
    return self.client.post(
        'api/v2/auth/login',
        data=json.dumps(dict(
            username='kamar',
            password='password123'
        )),
        content_type='application/json'
    )

def login_admin(self):
    """helper function for login an admin."""
    return self.client.post(
        'api/v2/auth/login',
        data=json.dumps(dict(
            username='admin',
            password='password123'
        )),
        content_type='application/json'
    )
