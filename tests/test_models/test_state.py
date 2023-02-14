#!/usr/bin/python3

'''This module contains the unittest for the State class'''


from models.base_model import BaseModel
from models.state import State
from unittest import TestCase
from unittest import main


class TestState(TestCase):
    '''The unittest class for the State class'''

    def test_init(self):
        '''Test the [__init__] function'''
        State1 = State()

        self.assertIsInstance(State1, State)
        self.assertIsInstance(State1.name, str)

        # test attributes values
        self.assertEqual(State1.name, "")
        State1.name = "Awka"

        self.assertEqual(State1.name, "Awka")

    def test_to_dict(self):
        '''Test the [to_dict] function'''
        State1 = State()
        State1.name = "Awka"
        State_to_dict = State1.to_dict()

        self.assertIn('created_at', State_to_dict)
        self.assertIn('updated_at', State_to_dict)
        self.assertIn('id', State_to_dict)
        self.assertIn('name', State_to_dict)
        self.assertIn('__class__', State_to_dict)

        self.assertEqual(State_to_dict['__class__'], 'State')
        self.assertIsInstance(State_to_dict['created_at'], str)
        self.assertIsInstance(State_to_dict['updated_at'], str)

    def test_str(self):
        '''Test for the __str__ method'''
        bm = State()
        expected = f"[State] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)


if __name__ == "__main__":
    main()
