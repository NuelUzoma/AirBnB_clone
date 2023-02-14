#!/usr/bin/python3

'''This module contains the unittest for the Review class'''


from models.base_model import BaseModel
from models.review import Review
from unittest import TestCase
from unittest import main


class TestReview(TestCase):
    '''The unittest class for the Review class'''

    def test_init(self):
        '''Test the [__init__] function'''
        Review1 = Review()

        self.assertIsInstance(Review1, Review)
        self.assertIsInstance(Review1.place_id, str)
        self.assertIsInstance(Review1.user_id, str)
        self.assertIsInstance(Review1.text, str)

        # test attributes values
        self.assertEqual(Review1.place_id, "")
        self.assertEqual(Review1.user_id, "")
        self.assertEqual(Review1.text, "")
        Review1.place_id = "place_id"
        Review1.user_id = "user_id"
        Review1.text = "Nice place"

        self.assertEqual(Review1.place_id, "place_id")
        self.assertEqual(Review1.user_id, "user_id")
        self.assertEqual(Review1.text, "Nice place")

    def test_to_dict(self):
        '''Test the [to_dict] function'''
        Review1 = Review()
        Review1.place_id = "place_id"
        Review1.user_id = "user_id"
        Review1.text = "Nice place"
        Review_to_dict = Review1.to_dict()

        self.assertIn('created_at', Review_to_dict)
        self.assertIn('updated_at', Review_to_dict)
        self.assertIn('id', Review_to_dict)
        self.assertIn('place_id', Review_to_dict)
        self.assertIn('user_id', Review_to_dict)
        self.assertIn('text', Review_to_dict)
        self.assertIn('__class__', Review_to_dict)

        self.assertEqual(Review_to_dict['__class__'], 'Review')
        self.assertIsInstance(Review_to_dict['created_at'], str)
        self.assertIsInstance(Review_to_dict['updated_at'], str)

    def test_str(self):
        '''Test for the __str__ method'''
        bm = Review()
        expected = f"[Review] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)


if __name__ == "__main__":
    main()
