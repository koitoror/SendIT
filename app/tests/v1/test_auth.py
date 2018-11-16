import unittest
from .base import BaseTestCase
from .helpers import login_user


class AuthTestCase(BaseTestCase):
    "Class for testing auth"

    def test_user_cannot_login_without_registration(self):
        with self.client:

            # logs in an unregistered user
            rv = login_user(self)
            self.assertEqual(rv.status_code, 401)
            self.assertIn(b'No user found. Please sign up', rv.data)


if __name__ == '__main__':
    unittest.main()
