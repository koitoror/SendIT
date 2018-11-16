import json

from .base import BaseTestCase


class TestParcel(BaseTestCase):
    """Test Parcels Endpoints."""

    def create(self):
        """Create parcel with required fields (parcel_name, price, present_location)."""
        return self.client.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')

    def create_no_parcel_name(self):
        """Create parcel with no parcel_name."""
        return self.client.post('/api/v1/parcels', data=json.dumps(self.no_parcel_name), content_type='application/json')

    def create_no_price(self):
        """Create parcel with no price."""
        return self.client.post('/api/v1/parcels', data=json.dumps(self.no_price), content_type='application/json')

    def create_no_json_data(self):
        """Create no json data"""
        return self.client.post('/api/v1/parcels', data=json.dumps(self.data))

    def test_create_parcel(self):
        """Test create parcel endpoint
        """
        with self.client:
            res = self.create()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(headers=headers)

            self.assertEqual(res.status_code, 201)
            self.assertIn(b"test1",res.data)

    def test_get_parcels(self):
        """Test get parcel endpoint
        """
        with self.client:
            res = self.create()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(headers=headers)

            self.assertEqual(res.status_code, 201)
            res = self.client.get('/api/v1/parcels', content_type='application/json')
            self.assertEqual(res.status_code, 200)
            self.assertIn(b"test",res.data )

    def test_get_one_parcel(self):
        """Test get_one parcel endpoint
        """
        with self.client:
            res = self.create()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(headers=headers)

            self.assertEqual(res.status_code, 201)
            result = self.client.get('/api/v1/parcels/{}'.format(res.get_json()['id']))
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"test",result.data )

    def test_delete_parcel(self):
        """Test delete parcel endpoint
        """
        with self.client:
            res = self.create()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post('/api/v1/parcels/', data=json.dumps(self.data), content_type='application/json', headers=headers)

            self.assertEqual(res.status_code, 201)
            result = self.client.delete('/api/v1/parcels/{}'.format(res.get_json()['id']))

            self.assertEqual(result.status_code, 204)
            self.assertNotIn(b'test', result.data)
            res = self.client.get('/api/v1/parcels/')
            self.assertEqual(res.status_code, 404)

    def test_update_parcel(self):
        """Test update parcel endpoint
        """
        with self.client:
            res = self.create()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(headers=headers)
            
            self.assertEqual(res.status_code, 201)
            result = self.client.put(
                '/api/v1/parcels/{}'.format(res.get_json()['id']),
                data=json.dumps({"parcel_name":"soccer-balls", "price":1000, "present_location":20}),
                content_type='application/json'
            )

            self.assertEqual(result.status_code, 200)
            self.assertIn(b"soccer-balls",result.data )

    def test_add_parcel_without_parcel_name(self):
        """Test add parcel without parcel_name."""
        with self.client:
            res = self.create_no_parcel_name()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(headers=headers)

            self.assertEqual(res.status_code, 400)
            parcel_name = res.get_json()['errors']['parcel_name']
            message = res.get_json()['message']
            self.assertIn("parcel_name should be a string Missing required parameter", parcel_name)
            self.assertIn("Input payload validation failed", message)

    def test_add_parcel_without_price(self):
        """Test add parcel without price."""
        with self.client:
            res = self.create_no_price()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(headers=headers)

            self.assertEqual(res.status_code, 400)
            price = res.get_json()['errors']['price']
            message = res.get_json()['message']
            self.assertIn("price should be a integer Missing required parameter", price)
            self.assertIn("Input payload validation failed", message)

    def test_add_no_json_data(self):
        "Test cannot add no json data"
        with self.client:
            res = self.create_no_json_data()

            access_token = 'mytoken'
            headers = {'Authorizations': 'Bearer {}'.format(access_token)}       
            return self.client.post(headers=headers)
            
            self.assertTrue(res.status_code, 400)
            message = res.get_json()['message']
            self.assertIn('Input payload validation failed', message)