import json

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
