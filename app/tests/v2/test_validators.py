import json
from app.tests.v2.base import BaseTestCase
from app.tests.v2.helpers import register_user, login_user, register_admin, login_admin


class TestValidatorsCase(BaseTestCase):
    "Class for testing validators"

    def test_username_is_required(self):
        """test username is a required field."""
        res = self.client.post(
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
            data=json.dumps(dict(
                username='kamar',
                email='kamardanielmoffatngiggelucaamugogokinya@gmail.com',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
            'api/v2/auth/signup',
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
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel_no_parcel_name
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"parcel_name is a required field", rv.data)

    def test_status_is_required(self):
        "Test status is a required property"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel_no_status
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"status is a required field", rv.data)

    def test_non_digit_status(self):
        "test for non-digit status."
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "first test",
                     "pickup_location": "DROP VAN",
                     "destination_location": "MOMBASA",
                     "price": 1000,
                     "status": "11111111"
                     })
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter non digit status", rv.data)

    def test_valid_status(self):
        "test status entered in valid format"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "first test",
                     "pickup_location": "DROP VAN",
                     "destination_location": "MOMBASA",
                     "price": 1000,
                     "status": "    "
                     })
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter valid status", rv.data)

    def test_valid_parcel_name(self):
        "test parcel_name entered in valid format"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"parcel_name": "    ",
                     "pickup_location": "DROP VAN",
                     "destination_location": "MOMBASA",
                     "price": 1000,
                     "status": "this is very awsome"
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
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps({
                    "parcel_name": "thelongparcel_namemorethanfiftycharacters",
                    "pickup_location": "DROP VAN",
                    "destination_location": "MOMBASA",
                    "price": 1000,
                    "status": "this is very awsome"
                    })
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"parcel_name is too long", rv.data)

    def test_parcel_destination_location_length(self):
        "test destination_location is less than 50 characters"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel
            )
            self.assertEqual(rv.status_code, 201)
            self.assertIn(b"Parcel added successfully", rv.data)

            # change parcel destination by making a PUT request
            rv = self.client.put(
                'api/v2/parcels/1/destination',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps({
                    "destination_location": "thelongparcel_namemorethanfiftycharacters"
                    })
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"destination_location is too long", rv.data)

    def test_parcel_cancel_length(self):
        "test cancel status is less than 50 characters"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel
            )
            self.assertEqual(rv.status_code, 201)
            self.assertIn(b"Parcel added successfully", rv.data)

            # change parcel status by making a PUT request
            rv = self.client.put(
                'api/v2/parcels/1/cancel',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps({
                    "status": "thelongparcel_namemorethanfiftycharacters"
                    })
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"status is too long", rv.data)
 
    def test_parcel_present_location_length(self):
        "test present_location is less than 50 characters"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel
            )
            self.assertEqual(rv.status_code, 201)
            self.assertIn(b"Parcel added successfully", rv.data)

            # change parcel destination by making a PUT request
            register_admin(self)
            res = login_admin(self)
            access_token = res.get_json()['token']
            
            rv = self.client.put(
                'api/v2/parcels/1/presentLocation',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps({
                    "present_location": "111111"
                    })
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter non digit present_location", rv.data)

    def test_parcel_status_length(self):
        "test status is less than 50 characters"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create parcel by making a POST request
            rv = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel
            )
            self.assertEqual(rv.status_code, 201)
            self.assertIn(b"Parcel added successfully", rv.data)

            # change parcel destination by making a PUT request
            register_admin(self)
            res = login_admin(self)
            access_token = res.get_json()['token']
            
            rv = self.client.put(
                'api/v2/parcels/1/status',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps({
                    "status": "111111"
                    })
            )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter non digit status", rv.data)
