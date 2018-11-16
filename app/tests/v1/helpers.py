import json


def register_user(self):
    """helper function for registering a user."""
    return self.client.post(
        'api/v1/auth/signup',
        data=json.dumps({
            "confirm": "password123",
            "password": "password123",
            "email": 'kamardaniel@gmail.com',
            "username": "kamar"
        }),
        content_type='application/json'
    )


def login_user(self):
    """helper function for login a user."""
    return self.client.post(
        'api/v1/auth/login',
        data=json.dumps({
            "password": "password123",
            "username": "kamar"
        }),
        content_type='application/json'
    )
