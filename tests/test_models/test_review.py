#!/usr/bin/python3
"""this is test for revieuw"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestReviewFile(unittest.TestCase):
    """test review file"""

    def setUp(self):
        self.rev = Review()
        self.rev.user_id = str(uuid.uuid4())

    def test_check_type(self):
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(isinstance(self.rev, Review))

    def test_idd(self):
        self.assertTrue(type(self.rev.user_id), str)
        self.assertTrue(type(self.rev.text), str)
        self.assertTrue(type(self.rev.updated_at), datetime)
        self.assertTrue(type(self.rev.created_at), datetime)

    def test_value(self):
        self.assertFalse(None, self.rev.__dict__.values())

    def test_attr(self):
        self.assertTrue(hasattr(self.rev, 'id'))
        self.assertTrue(hasattr(self.rev, 'created_at'))
        self.assertTrue(hasattr(self.rev, 'updated_at'))
        self.assertTrue(hasattr(self.rev, 'user_id'))
        self.assertTrue(hasattr(self.rev, 'place_id'))
        self.assertTrue(hasattr(self.rev, 'text'))

    def test_dict(self):
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)

    def test_tedupcr(self):
        self.rev2 = Review()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)
        self.assertNotEqual(self.rev.id, self.rev2.id)


if __name__ == '__main__':
    unittest.main()
