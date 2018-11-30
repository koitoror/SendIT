import json

from .base import BaseTestCase
from .helpers import register_user, login_user, login_admin


class TestParcel(BaseTestCase):
    """Test Parcels Endpoints."""

    def create(self):
        """Create parcel with required fields
        (parcel_name, price, present_location, destination_location)."""
        
        res = register_user(self)
        self.assertTrue(res.status_code, 201)
        res = login_user(self)
        access_token = res.get_json()['token']

        headers = {
                "x-access-token": access_token,
                "content-type": "application/json"
        }
         
        return self.client.post('/api/v1/parcels',
                                data=json.dumps(self.parcel),
                                headers=headers,
                                content_type='application/json')

    def create_no_parcel_name(self):
        """Create parcel with no parcel_name."""

        res = register_user(self)
        self.assertTrue(res.status_code, 201)
        res = login_user(self)
        access_token = res.get_json()['token']

        headers = {
                "x-access-token": access_token,
                "content-type": "application/json"
        }

        return self.client.post('/api/v1/parcels',
                                data=json.dumps(self.no_parcel_name),
                                headers=headers,
                                content_type='application/json')

    def create_no_price(self):
        """Create parcel with no price."""

        res = register_user(self)
        self.assertTrue(res.status_code, 201)
        res = login_user(self)
        access_token = res.get_json()['token']

        headers = {
                "x-access-token": access_token,
                "content-type": "application/json"
        }

        return self.client.post('/api/v1/parcels',
                                data=json.dumps(self.no_price),
                                headers=headers,
                                content_type='application/json')

    def create_no_json_data(self):
        """Create no json data"""

        res = register_user(self)
        self.assertTrue(res.status_code, 201)
        res = login_user(self)
        access_token = res.get_json()['token']

        headers = {
                "x-access-token": access_token
        }
        return self.client.post('/api/v1/parcels',
                                headers=headers,
                                data=json.dumps(self.parcel))

    def test_create_parcel(self):
        """Test create parcel endpoint
        """
        with self.client:
            res = self.create()

            self.assertEqual(res.status_code, 201)
            self.assertIn(b"TRAVEL BAG", res.data)

    def test_get_parcels(self):
        """Test get parcel endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)

            res = login_user(self)
            access_token = res.get_json()['token']
            headers = {
                    "x-access-token": access_token,
                    "content-type": "application/json"
            }

            res = self.client.get('/api/v1/parcels',
                                  headers=headers,
                                  content_type='application/json')
            self.assertEqual(res.status_code, 200)
            self.assertIn(b"null", res.data)

    def test_get_one_parcel(self):
        """Test get_one parcel endpoint
        """
        with self.client:
            res1 = self.create()
            self.assertEqual(res1.status_code, 201)

            res = login_user(self)
            access_token = res.get_json()['token']
            headers = {
                    "x-access-token": access_token,
                    "content-type": "application/json"
            }
            result = self.client.get(
                '/api/v1/parcels/{}'.format(res1.get_json()['parcel_id']),
                headers=headers
                )

            self.assertEqual(result.status_code, 200)
            self.assertIn(b"TRAVEL BAG", result.data)

    def test_delete_parcel(self):
        """Test delete parcel endpoint
        """
        with self.client:
            res1 = self.create()
            self.assertEqual(res1.status_code, 201)

            res = login_user(self)
            access_token = res.get_json()['token']
            headers = {
                    "x-access-token": access_token,
                    "content-type": "application/json"
            }

            result = self.client.delete(
                '/api/v1/parcels/{}'.format(res1.get_json()['parcel_id']),
                content_type='application/json',
                headers=headers)

            self.assertEqual(result.status_code, 204)
            self.assertNotIn(b'test', result.data)
            res = self.client.get('/api/v1/parcels/')
            self.assertEqual(res.status_code, 404)

    def test_update_parcel(self):
        """Test update parcel endpoint
        """
        with self.client:
            res1 = self.create()
            self.assertEqual(res1.status_code, 201)

            res = login_user(self)
            access_token = res.get_json()['token']
            headers = {
                    "x-access-token": access_token,
                    "content-type": "application/json"
            }

            result = self.client.put(
                '/api/v1/parcels/{}'.format(res1.get_json()['parcel_id']),

                data=json.dumps({"present_location": "KAMWOSOR",
                                 "status": "IN TRANSIT"}),
                headers=headers,
                content_type='application/json'
            )

            self.assertEqual(result.status_code, 200)
            self.assertIn(b"IN TRANSIT", result.data)

    def test_add_parcel_without_parcel_name(self):
        """Test add parcel without parcel_name."""
        with self.client:
            res = self.create_no_parcel_name()

            self.assertEqual(res.status_code, 400)
            parcel_name = res.get_json()['errors']['parcel_name']
            message = res.get_json()['message']
            self.assertIn(
                "parcel_name should be a string Missing required parameter",
                parcel_name)
            self.assertIn("Input payload validation failed", message)

    def test_add_parcel_without_price(self):
        """Test add parcel without price."""
        with self.client:
            res = self.create_no_price()

            self.assertEqual(res.status_code, 400)
            price = res.get_json()['errors']['price']
            message = res.get_json()['message']
            self.assertIn(
                "price should be a integer Missing required parameter", price)
            self.assertIn("Input payload validation failed", message)

    def test_add_no_json_data(self):
        "Test cannot add no json data"
        with self.client:
            res = self.create_no_json_data()

            self.assertTrue(res.status_code, 400)
            message = res.get_json()['message']
            self.assertIn('Input payload validation failed', message)
