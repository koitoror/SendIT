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

# def create_parcel(self, access_token):
#     "helper function for creating an parcel"
#     rv = self.client.post(
#     'api/v1/parcels',
#     headers={
#         "x-access-token": access_token,
#         "content-type": "application/json"
#     },
#     data=json.dumps({
#         "parcel_name": "TRAVEL BAG", 
#         "pickup_location": "DROP VAN",
#         "destination_location": "MOMBASA",
#         "price": 1000
#         }),
#         content_type='application/json'
#     )

# def get_all(self, access_token):
#     "helper function for creating an parcel"
#     rv = self.client.get(
#     'api/v1/parcels',
#     headers={
#         "x-access-token": access_token,
#         "content-type": "application/json"
#     }
#     )