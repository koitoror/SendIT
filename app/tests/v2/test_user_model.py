import unittest

from app.tests.v2.base import BaseTestCase
from app.api.v2.models.user import User



class TestUserModel(BaseTestCase):

    def test_generate_token(self):
        token = User.generate_token(self.user.user_id)
        self.assertTrue(isinstance(token, bytes))

    def test_get_user_by_username(self):
        User.create_user(self.cursor, "kamardaniel", "kamar@gmail.com", "password")
        user = User.get_user_by_username(self.dict_cursor, "kamardaniel")
        self.assertIn('kamardaniel', user.values())


if __name__ == '__main__':
    unittest.main()