#!/usr/bin/python3

'''This module contains the unittest for the User class'''


from models.base_model import BaseModel
from models.user import User
from unittest import TestCase
from unittest import main


class TestUser(TestCase):
    '''The unittest class for the User class'''

    def test_init(self):
        '''Test the [__init__] function'''
        user1 = User()

        self.assertIsInstance(user1, User)
        self.assertIsInstance(user1.email, str)
        self.assertIsInstance(user1.first_name, str)
        self.assertIsInstance(user1.last_name, str)
        self.assertIsInstance(user1.password, str)

        # test attributes values
        self.assertEqual(user1.email, "")
        self.assertEqual(user1.first_name, "")
        self.assertEqual(user1.last_name, "")
        self.assertEqual(user1.password, "")
        user1.email = "test@gmail.com"
        user1.first_name = "Nuel"
        user1.last_name = "Jerry"
        user1.password = "test123"

        self.assertEqual(user1.email, "test@gmail.com")
        self.assertEqual(user1.first_name, "Nuel")
        self.assertEqual(user1.last_name, "Jerry")
        self.assertEqual(user1.password, "test123")

    def test_to_dict(self):
        '''Test the [to_dict] function'''
        user1 = User()
        user1.first_name = "jerry"
        user1.email = "test@gmail.com"
        user1.last_name = "Nuel"
        user1.password = "test123"
        user_to_dict = user1.to_dict()

        self.assertIn('created_at', user_to_dict)
        self.assertIn('updated_at', user_to_dict)
        self.assertIn('id', user_to_dict)
        self.assertIn('first_name', user_to_dict)
        self.assertIn('last_name', user_to_dict)
        self.assertIn('email', user_to_dict)
        self.assertIn('password', user_to_dict)
        self.assertIn('__class__', user_to_dict)

        self.assertEqual(user_to_dict['__class__'], 'User')
        self.assertIsInstance(user_to_dict['created_at'], str)
        self.assertIsInstance(user_to_dict['updated_at'], str)

    def test_str(self):
        '''Test for the __str__ method'''
        bm = User()
        expected = f"[User] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)


if __name__ == "__main__":
    main()
