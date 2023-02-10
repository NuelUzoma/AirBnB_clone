#!/usr/bin/python3

'''
A unittest for the base model class
'''


from datetime import datetime
import unittest
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Unittest for the base model
    '''
    def test_init(self):
        '''
        Test cases for the init method
        '''
        base1 = BaseModel()
        self.assertIsNotNone(base1)
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)
        self.assertNotEqual(base1.created_at, base1.updated_at)
        
        updated_at = '2017-09-28T21:03:54.052302'
        created_at = '2017-09-28T21:03:54.052298'
        baseid = uuid.uuid4().hex
        
        base2 = BaseModel(updated_at='2017-09-28T21:03:54.052302',
                          created_at='2017-09-28T21:03:54.052298',
                          id=baseid, __class__="basemodel")
        self.assertIsInstance(base2.id, str)
        self.assertIsInstance(base2.created_at, datetime)
        self.assertIsInstance(base2.updated_at, datetime)
        self.assertEqual(base2.created_at, datetime.fromisoformat(created_at))
        self.assertEqual(base2.updated_at, datetime.fromisoformat(updated_at))
        self.assertEqual(base2.id, baseid)
        with self.assertRaises(AttributeError):
            self.__class__

    def test_str(self):
        '''Test for the __str__ method'''
        updated_at = '2017-09-28T21:03:54.052302'
        created_at = '2017-09-28T21:03:54.052298'
        baseid = uuid.uuid4().hex
        base2 = BaseModel(updated_at='2017-09-28T21:03:54.052302',
                          created_at='2017-09-28T21:03:54.052298',
                          id=baseid, __class__="basemodel")
        
        

if __name__ == "__main__":
    unittest.main()