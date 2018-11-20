import unittest

from app.tests.v2.base import BaseTestCase

from app.api.v2.models.user import User
from app.api.v2.models.parcel import Parcel


class TestParcelModel(BaseTestCase):

    def test_get_parcel_by_id(self):
        User.create_user(self.cursor, "kamardaniel", "kamar@gmail.com", "password")
        Parcel.create_parcel(self.cursor, "first parcel model test", 1, "testing is very essential", "testing", "testing", 1)
        result = Parcel.get_parcel_by_id(self.dict_cursor, 1)
        self.assertIn("first parcel model test", result.values())

    def test_get_all_parcels(self):
        User.create_user(self.cursor, "kamardaniel", "kamar@gmail.com", "password")
        Parcel.create_parcel(self.cursor, "first parcel model test", 1, "testing is very essential", "testing", "testing", 1)
        result = Parcel.get_all(self.dict_cursor, 1)
        self.assertIn("first parcel model test", result[0].values())


if __name__ == '__main__':
    unittest.main()