#!/usr/bin/python3

'''This module contains the unittest for the Amenity class'''


from models.base_model import BaseModel
from models.amenity import Amenity
from unittest import TestCase
from unittest import main


class TestAmenity(TestCase):
    '''The unittest class for the Amenity class'''

    def test_init(self):
        '''Test the [__init__] function'''
        Amenity1 = Amenity()

        self.assertIsInstance(Amenity1, Amenity)
        self.assertIsInstance(Amenity1.name, str)

        # test attributes values
        self.assertEqual(Amenity1.name, "")
        Amenity1.name = "Electricity"

        self.assertEqual(Amenity1.name, "Electricity")

    def test_to_dict(self):
        '''Test the [to_dict] function'''
        Amenity1 = Amenity()
        Amenity1.name = "Awka"
        Amenity_to_dict = Amenity1.to_dict()

        self.assertIn('created_at', Amenity_to_dict)
        self.assertIn('updated_at', Amenity_to_dict)
        self.assertIn('id', Amenity_to_dict)
        self.assertIn('name', Amenity_to_dict)
        self.assertIn('__class__', Amenity_to_dict)

        self.assertEqual(Amenity_to_dict['__class__'], 'Amenity')
        self.assertIsInstance(Amenity_to_dict['created_at'], str)
        self.assertIsInstance(Amenity_to_dict['updated_at'], str)

    def test_str(self):
        '''Test for the __str__ method'''
        bm = Amenity()
        expected = f"[Amenity] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)


if __name__ == "__main__":
    main()
