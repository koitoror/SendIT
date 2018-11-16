import unittest

from .base import BaseTestCase
from app.api.v1.models.user import user_class


class TestUserModel(BaseTestCase):

    def test_generate_token(self):
        token = user_class.generate_token(self.user_class.user_id)
        self.assertTrue(isinstance(token, bytes))

    def test_get_user_by_username(self):
        new_user = {
            "confirm": "johndoe123",
            "password": "password",
            "email": "kamar@gmail.com",
            "username": "kamardaniel"   
        }
        
        user_class.create_user(new_user)
        user = user_class.get_user_by_username("kamardaniel")
        for x in user:
            self.assertIn('kamardaniel', x.values())


if __name__ == '__main__':
    unittest.main()