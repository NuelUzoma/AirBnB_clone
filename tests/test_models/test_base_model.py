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
        self.assertNotEqual(base1.id, base2.id)

        # test if attributes are being added
        attrs = {"my_name": "jerry", "car": "bentley"}
        base3 = BaseModel(**attrs)

        self.assertEqual(base3.my_name, "jerry")
        self.assertEqual(base3.car, "bentley")

        # test for correct values of created_at and updated_at
        base4 = BaseModel()
        base5 = BaseModel()

        now = datetime.now()

        self.assertLessEqual(base4.created_at, now)
        self.assertLessEqual(base4.updated_at, now)
        self.assertLessEqual(base5.created_at, now)
        self.assertLessEqual(base5.updated_at, now)

    def test_str(self):
        '''Test for the __str__ method'''
        bm = BaseModel()
        expected = f"[BaseModel] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected)

    def test_save(self):
        '''Test the [save] method of BaseModel class'''
        base1 = BaseModel()
        old_updated_at = base1.updated_at
        base1.save()

        self.assertLess(old_updated_at, base1.updated_at)

    def test_dict(self):
        '''Test the [to_dict] method of the BaseModel class'''
        base1 = BaseModel()
        base1.name = "jerry"
        base1.car = "bentley"

        base_dict = base1.to_dict()

        self.assertIn("id", base_dict)
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
