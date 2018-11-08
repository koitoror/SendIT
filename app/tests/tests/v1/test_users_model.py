import unittest

from .base import BaseTestCase
from app.api.v1.models.user import User as UserClass

users = UserClass()

class TestUserModel(BaseTestCase):

    def test_generate_token(self):
        token = users.generate_token(self.user.user_id)
        self.assertTrue(isinstance(token, bytes))

    def test_get_user_by_username(self):
        new_user = {
            "confirm": "johndoe123",
            "password": "password",
            "email": "kamar@gmail.com",
            "username": "kamardaniel"   
        }
        
        users.create_user(new_user)
        user = users.get_user_by_username("kamardaniel")
        for x in user:
            self.assertIn('kamardaniel', x.values())


if __name__ == '__main__':
    unittest.main()