# import unittest

# from .base import BaseTestCase
# from app.api.v1.models.parcel import parcel_class


# class TestparcelModel(BaseTestCase):

#     # def test_generate_token(self):
#     #     token = parcel_class.generate_token(self.parcel_class.parcel_id)
#     #     self.assertTrue(isinstance(token, bytes))

#     def test_create_parcel(self):
#         new_parcel = {
#             "parcel_name": "TRAVEL BAG", 
#             "pickup_location": "DROP VAN",
#             "destination_location": "MOMBASA",
#             "price": 1000
#         }
        
#         parcel_class.create_parcel_test(new_parcel)
#         # parcel = parcel_class.create_parcel_test("kamardaniel")
#         # for x in parcel:
#         self.assertIn('kamardaniel', x.values())


# if __name__ == '__main__':
#     unittest.main()