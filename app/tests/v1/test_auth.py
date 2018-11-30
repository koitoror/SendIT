import unittest
import json
from .base import BaseTestCase
from .helpers import login_user, register_user, login_admin


class AuthTestCase(BaseTestCase):
    "Class for testing auth"

    def test_user_registration(self):
        with self.client:
            # registering a user
            res = register_user(self)
            self.assertEqual(res.status_code, 201)

    def test_user_cannot_register_twice(self):
        with self.client:
            # registering a user
            res = register_user(self)
            self.assertEqual(res.status_code, 201)

        # test second registration
        with self.client:
            res = register_user(self)
            self.assertEqual(res.status_code, 400)
            self.assertIn(
                b'Email exists, please login or register',
                res.data)

    def test_user_login(self):
        with self.client:
            # registering a user
            res = register_user(self)
            self.assertEqual(res.status_code, 201)

            # logs in a user
            rv = login_user(self)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'token', rv.data)

    def test_user_cannot_login_without_registration(self):
        with self.client:

            # logs in an unregistered user
            rv = login_user(self)
            self.assertEqual(rv.status_code, 401)
            self.assertIn(b'No user found. Please sign up', rv.data)
    
    def test_user_with_incorrect_credentials(self):
        with self.client:
            # registering a user
            res = register_user(self)
            self.assertEqual(res.status_code, 201)

            # loging a user with incorrect credentials
            rv = self.client.post(
                '/api/v1/auth/login',
                data=json.dumps(dict(
                    username='kamar',
                    password='password'
                )),
                content_type='application/json'
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b'Invalid password', rv.data)


if __name__ == '__main__':
    unittest.main()
