#!/usr/bin/python3

'''This module contains the unittest for the Place class'''


from models.base_model import BaseModel
from models.place import Place
from unittest import TestCase
from unittest import main


class TestPlace(TestCase):
    '''The unittest class for the Place class'''

    def test_init(self):
        '''Test the [__init__] function'''
        Place1 = Place()

        self.assertIsInstance(Place1, Place)
        self.assertIsInstance(Place1.city_id, str)
        self.assertIsInstance(Place1.user_id, str)
        self.assertIsInstance(Place1.amenity_ids, list)
        self.assertIsInstance(Place1.name, str)
        self.assertIsInstance(Place1.description, str)
        self.assertIsInstance(Place1.latitude, float)
        self.assertIsInstance(Place1.longitude, float)
        self.assertIsInstance(Place1.number_bathrooms, int)
        self.assertIsInstance(Place1.number_rooms, int)
        self.assertIsInstance(Place1.price_by_night, int)
        self.assertIsInstance(Place1.max_guest, int)

        # test attributes values
        self.assertEqual(Place1.city_id, "")
        self.assertEqual(Place1.user_id, "")
        self.assertEqual(Place1.amenity_ids, [])
        self.assertEqual(Place1.name, "")
        self.assertEqual(Place1.description, "")
        self.assertEqual(Place1.latitude, 0.0)
        self.assertEqual(Place1.longitude, 0.0)
        self.assertEqual(Place1.number_bathrooms, 0)
        self.assertEqual(Place1.number_rooms, 0)
        self.assertEqual(Place1.price_by_night, 0)
        self.assertEqual(Place1.max_guest, 0)

        Place1.city_id = "city_id"
        Place1.user_id = "user_id"
        Place1.amenity_ids = ["amenity_id"]
        Place1.name = "Awka"
        Place1.description = "Nice place"
        Place1.latitude = 1.1
        Place1.longitude = 1.2
        Place1.number_bathrooms = 3
        Place1.number_rooms = 2
        Place1.price_by_night = 10000
        Place1.max_guest = 13

        self.assertEqual(Place1.city_id, "city_id")
        self.assertEqual(Place1.user_id, "user_id")
        self.assertEqual(Place1.amenity_ids, ["amenity_id"])
        self.assertEqual(Place1.name, "Awka")
        self.assertEqual(Place1.description, "Nice place")
        self.assertEqual(Place1.latitude, 1.1)
        self.assertEqual(Place1.longitude, 1.2)
        self.assertEqual(Place1.number_bathrooms, 3)
        self.assertEqual(Place1.number_rooms, 2)
        self.assertEqual(Place1.price_by_night, 10000)
        self.assertEqual(Place1.max_guest, 13)

    def test_to_dict(self):
        '''Test the [to_dict] function'''
        Place1 = Place()
        Place1.city_id = "city_id"
        Place1.user_id = "user_id"
        Place1.amenity_ids = ["amenity_id"]
        Place1.name = "Awka"
        Place1.description = "Nice place"
        Place1.latitude = 1.1
        Place1.longitude = 1.2
        Place1.number_bathrooms = 3
        Place1.number_rooms = 2
        Place1.price_by_night = 10000
        Place1.max_guest = 10
        Place_to_dict = Place1.to_dict()

        self.assertIn('created_at', Place_to_dict)
        self.assertIn('updated_at', Place_to_dict)
        self.assertIn('id', Place_to_dict)
        self.assertIn('city_id', Place_to_dict)
        self.assertIn('user_id', Place_to_dict)
        self.assertIn('amenity_ids', Place_to_dict)
        self.assertIn('name', Place_to_dict)
        self.assertIn('description', Place_to_dict)
        self.assertIn('latitude', Place_to_dict)
        self.assertIn('longitude', Place_to_dict)
        self.assertIn('number_bathrooms', Place_to_dict)
        self.assertIn('number_rooms', Place_to_dict)
        self.assertIn('price_by_night', Place_to_dict)
        self.assertIn('max_guest', Place_to_dict)
        self.assertIn('__class__', Place_to_dict)

        self.assertEqual(Place_to_dict['__class__'], 'Place')
        self.assertIsInstance(Place_to_dict['created_at'], str)
        self.assertIsInstance(Place_to_dict['updated_at'], str)

    def test_str(self):
        '''Test for the __str__ method'''
        bm = Place()
        expected = f"[Place] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)


if __name__ == "__main__":
    main()
