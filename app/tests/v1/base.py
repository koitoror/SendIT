from flask_testing import TestCase
from app.api.v1.models.parcel import parcel_class
from app.api.v1.models.user import user_class

from run import app


class BaseTestCase(TestCase):
    """ Base Tests """

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def setUp(self):
        self.user_class = user_class
        self.user = self.user_class.create_user({
            "confirm": "johndoe123",
            "password": "johndoe123",
            "email": "johndoe@gmail.com",
            "username": "johndoe"
        })

        self.user_class.user_id = ''

        self.parcel_class = parcel_class
        self.parcel = self.parcel_class.create_parcel_test({
            "parcel_name": "TRAVEL BAG",
            "pickup_location": "DROP VAN",
            "destination_location": "MOMBASA",
            "status": "IN TRANSIT",
            "price": 1000
        })

        self.parcel_class = parcel_class
        self.no_parcel_name = self.parcel_class.create_parcel_test({
            "pickup_location": "DROP VAN",
            "destination_location": "MOMBASA",
            
            "price": 1000
        })

        self.parcel_class = parcel_class
        self.no_price = self.parcel_class.create_parcel_test({
            "parcel_name": "TRAVEL BAG",
            "pickup_location": "DROP VAN",
            "destination_location": "MOMBASA"

        })

        self.parcel_class = parcel_class
        self.no_destination_location = self.parcel_class.create_parcel_test({
            "parcel_name": "TRAVEL BAG",
            "pickup_location": "DROP VAN",
            "destination_location": " ",
            "price": 1000
        })

    def tearDown(self):
        self.user_class.no_of_users.clear()
        self.parcel_class.no_of_parcels.clear()
