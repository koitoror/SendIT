""""Application Product Point."""

import os
import unittest

"""Handles database migrations"""
import re
import sys
from app.database import Database
db = Database()
cursor = db.cursor
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


# third-party imports
from flask_bcrypt import Bcrypt
from flask_script import Manager # controller class for handling commands
from flask_script import prompt, prompt_pass
from flask_cors import CORS


# local imports
from app import create_app
from app.api.v2.models.user import User


# application development instance
app = create_app(config_name=os.getenv("FLASK_CONFIG"))
CORS(app)

# initializing the manager object
manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)

@manager.command
def test():
    test = unittest.TestLoader().discover("./app/tests", pattern="test*.py")
    unittest.TextTestRunner(verbosity=2).run(test)

@manager.command
def createadmin():
    """Create a admin, requires username, email and password."""
    db.create_tables()
    username = prompt('admin username')
    email = prompt('admin email')
    confirm_email = prompt('confirm admin email')

    if not EMAIL_REGEX.match(email):
        sys.exit('\n kindly provide a valid email address')
    if not email == confirm_email:
        sys.exit('\n kindly ensure that email and confirm email are identical')

    password = prompt_pass('admin password')
    confirm = prompt_pass('confirm admin password')

    if len(password) < 8:
        sys.exit('\n kindly ensure that the password is at leaast 8 characters long')
    if not password == confirm:
        sys.exit('\n kindly ensure that password and confirm password are identical')
    hash_password = Bcrypt().generate_password_hash(password).decode()
    admin = True

    User.create_admin(cursor, username=username, email=email, password=hash_password, admin=admin)
    sys.exit('\n admin successfully created')

if __name__ == "__main__":
    manager.run()
