import unittest

from app.tests.v1.base import BaseTestCase

from app.api.v1.models.user import user_class
from app.api.v1.models.parcel import parcel_class


class TestParcelModel(BaseTestCase):

    def test_get_parcel_by_id(self):
        user = {
            "confirm": "password",
            "password": "password",
            "email": "kamar@gmail.com",
            "username": "kamardaniel"
        }
        user_class.create_user(user)
        parcel = {
            "parcel_name": "TRAVEL BAG",
            "pickup_location": "DROP VAN",
            "destination_location": "MOMBASA",
            "price": 1000
        }
        parcel_class.create_parcel(parcel, 2)

        result = parcel_class.get_one(1, 2)
        for x in result:
            self.assertIn("TRAVEL BAG", x.values())

if __name__ == '__main__':
    unittest.main()
