import unittest
from .base import BaseTestCase
from .helpers import register_user, register_admin, login_user, login_admin


class ParcelsTestCase(BaseTestCase):
    """Represents the parcels test case"""

    def test_parcel_creation(self):
        """Test API can create a parcel.""" 

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
            self.assertIn(b'Parcel added successfully', rv.data)

    # def test_api_can_get_all_parcels(self):
    #     """Test API can get all."""
    #     with self.client:

    #         res = register_admin(self)
    #         self.assertTrue(res.status_code, 201)
    #         res = login_admin(self)
    #         access_token = res.get_json()['token']

    #         # create a parcel
    #         res = self.client.post(
    #             'api/v2/parcels',
    #             headers={
    #                 "x-access-token": access_token,
    #                 "content-type": "application/json"
    #             },
    #             data=self.parcel
    #             )
    #         self.assertEqual(res.status_code, 201)

    #         # get all the parcels that belong to all users
    #         # login_admin(self)
    #         res = login_admin(self)
    #         access_token = res.get_json()['token']

    #         res = self.client.get(
    #             'api/v2/parcels',
    #              headers={
    #                 "x-access-token": access_token,
    #                 "content-type": "application/json"
    #             },
    #         )
    #         self.assertEqual(res.status_code, 200)
    #         self.assertIn(b'first test', res.data)

    def test_api_can_get_parcel_by_id(self):
        """Test API can get a single parcel by using it's id."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create a parcel
            res = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel
                )
            self.assertEqual(res.status_code, 201)

            # get all the parcels by a specific id
            res = self.client.get(
                'api/v2/parcels/1',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'first test', res.data)

    def test_parcel_can_be_edited(self):
        """Test API can edit an existing parcel. (PUT request)"""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create a parcel
            res = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel
                )
            self.assertEqual(res.status_code, 201)

            # modify a parcel
            rv = self.client.put(
                '/api/v2/parcels/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.update_parcel
                )
            self.assertEqual(rv.status_code, 200)

            res = self.client.get(
                'api/v2/parcels/1',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertIn(b'first edition', res.data)

    def test_parcel_deletion(self):
        """Test API can delete an existing parcel."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create a parcel
            res = self.client.post(
                'api/v2/parcels',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.parcel
                )
            self.assertEqual(res.status_code, 201)
            
            # delete a parcel
            res = self.client.delete(
                '/api/v2/parcels/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                }
                )
            self.assertTrue(res.status_code, 200)
            self.assertIn(b"Parcel deleted successully", res.data)
            # test for Parcel order not found
            res = self.client.get(
                '/api/v2/parcels/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                }
                )
            self.assertEqual(res.status_code, 404)
            self.assertIn(b"Parcel 1 not found", res.data)

if __name__ == "__main__":
    unittest.main()