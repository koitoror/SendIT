from flask_testing import TestCase
from app.api.v1.models.parcel import Parcel
from app.api.v1.models.user import User

from run import app


class BaseTestCase(TestCase):
    """ Base Tests """

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def setUp(self):
        self.user = User()
        self.data = self.user.create_user({
            "confirm": "johndoe123",
            "password": "johndoe123",
            "email": "johndoe@gmail.com",
            "username": "johndoe"
            })

        self.user.user_id = ''

        self.parcel = Parcel()
        self.data = self.parcel.create_parcel({
            "parcel_name": "TRAVEL BAG", 
            "pickup_location": "DROP VAN",
            "destination_location": "MOMBASA",
            "price": 1000
            })
        
        self.no_parcel_name = self.parcel.create_parcel({
            "parcel_name": " ", 
            "pickup_location": "DROP VAN",
            "destination_location": "MOMBASA",
            "price": 1000
            })

        self.no_price = self.parcel.create_parcel({
            "parcel_name": "TRAVEL BAG", 
            "pickup_location": "DROP VAN",
            "destination_location": "MOMBASA"

            })

        self.no_destination_location = self.parcel.create_parcel({
            "parcel_name": "TRAVEL BAG", 
            "pickup_location": "DROP VAN",
            "destination_location": " ",
            "price": 1000
            })

    def tearDown(self):
        self.user.no_of_users.clear()
        self.parcel.no_of_parcels.clear()