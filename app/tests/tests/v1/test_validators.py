import json
from .base import BaseTestCase
from .helpers import register_user, login_user

class TestValidatorsCase(BaseTestCase):
    "Class for testing validators"

    def test_username_is_required(self):
        """test username is a required field."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            username='',
            email='kamardaniel@gmail.com',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"username is a required field", res.data)

    def test_username_length(self):
        """test username requires at most 10 characters."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            username='kamardaniel1kamardaniel2',
            email='kamardaniel@gmail.com',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"username is too long", res.data)

    def test_email_length(self):
        """test email is a required field."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            username='kamar',
            email='kamardanielmoffatngiggelucaamugogokinyakinyanjui@gmail.com',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"email is too long", res.data)

    def test_email_is_required(self):
        """test email is a required field."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            username='kamar',
            email='',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"email is a required field", res.data)

    def test_password_is_required(self):
        """test password is a required field."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            email='kamardaniel@gmail.com',
            username='kamar',
            password='',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"password is a required field", res.data)

    def test_password_is_valid(self):
        """test password is not whitespace."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            email='kamardaniel@gmail.com',
            username='kamar',
            password='      ',
            confirm='      '
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a valid password", res.data)

    def test_password_requires_6_characters(self):
        """test password requires atleast six characters."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            email='kamardaniel@gmail.com',
            username='kamar',
            password='pass',
            confirm='pass'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"password requires atlest 6 characters", res.data)

    def test_valid_email_format(self):
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            email='kamardanielgmail.com',
            username='kamar',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a valid email address", res.data)

    def test_password_must_match_to_register(self):
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            email='kamardaniel@gmail.com',
            username='kamar',
            password='passwor',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"password mismatch", res.data)

    def test_non_digit_username(self):
        """test non-digit username."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            email='kamardaniel@gmail.com',
            username='12345',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a non digit username", res.data)

    def test_valid_username(self):
        """test valid username format."""
        res = self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            email='kamardaniel@gmail.com',
            username='      ',
            password='password123',
            confirm='password123'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a valid username", res.data)

    def test_parcel_name_is_required(self):
        "Test parcel_name is a required property"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v1/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": " ",
                    # "status": "11111111",
                    "pickup_location": "DROP VAN",
                    "destination_location": "11111111",
                    "price": 1000
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"parcel_name is a required field", rv.data)

    def test_destination_location_is_required(self):
        "Test status is a required property"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v1/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "first test",
                    # "status": "11111111",
                    "pickup_location": "DROP VAN",
                    "destination_location": " ",
                    "price": 1000
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"destination_location is a required field", rv.data)

    def test_non_digit_destination_location(self):
        "test for non-digit destination_location."
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v1/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "first test",
                    # "status": "11111111",
                    "pickup_location": "DROP VAN",
                    "destination_location": "11111111",
                    "price": 1000
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter non digit destination_location", rv.data)

    def test_valid_destination_location(self):
        "test destination_location entered in valid format"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v1/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "first test",
                    # "status": "    ",
                    "pickup_location": "DROP VAN",
                    "destination_location": "    ",
                    "price": 1000
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter valid destination_location", rv.data)

    def test_valid_parcel_name(self):
        "test parcel_name entered in valid format"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v1/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "    ",
                    "status": "this is very awsome",
                    "pickup_location": "DROP VAN",
                    "destination_location": "MOMBASA",
                    "price": 1000
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter a valid parcel_name", rv.data)

    def test_parcel_name_length(self):
        "test parcel_name is less than 50 characters"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v1/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "thisisthelongestparcel_nameeveranitshouldbemorethanfiftycharacterslong",
                    "pickup_location": "DROP VAN",
                    "destination_location": "MOMBASA",
                    "price": 1000
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"parcel_name is too long", rv.data)
