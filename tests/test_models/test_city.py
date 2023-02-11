#!/usr/bin/python3

'''This module contains the unittest for the City class'''


from models.base_model import BaseModel
from models.city import City
from unittest import TestCase
from unittest import main


class TestCity(TestCase):
    '''The unittest class for the City class'''

    def test_init(self):
        '''Test the [__init__] function'''
        City1 = City()

        self.assertIsInstance(City1, City)
        self.assertIsInstance(City1.state_id, str)
        self.assertIsInstance(City1.name, str)

        # test attributes values
        self.assertEqual(City1.name, "")
        City1.name = "Awka"
        City1.state_id = "id1"

        self.assertEqual(City1.name, "Awka")
        self.assertEqual(City1.state_id, "id1")

    def test_to_dict(self):
        '''Test the [to_dict] function'''
        City1 = City()
        City1.name = "Awka"
        City1.state_id = "id1"
        City_to_dict = City1.to_dict()

        self.assertIn('created_at', City_to_dict)
        self.assertIn('updated_at', City_to_dict)
        self.assertIn('id', City_to_dict)
        self.assertIn('name', City_to_dict)
        self.assertIn('state_id', City_to_dict)
        self.assertIn('__class__', City_to_dict)

        self.assertEqual(City_to_dict['__class__'], 'City')
        self.assertIsInstance(City_to_dict['created_at'], str)
        self.assertIsInstance(City_to_dict['updated_at'], str)

    def test_str(self):
        '''Test for the __str__ method'''
        bm = City()
        expected = f"[City] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)


if __name__ == "__main__":
    main()
