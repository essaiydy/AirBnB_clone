#!/usr/bin/python3
"""unittest of file storage"""

import unittest
from models.engine.file_storage import FileStorage
from models import storage


class FileStorage(unittest.TestCase):
    """all test of this class is here"""

    def setUp(self):
        instt = FileStorage()

    def test_instante(self):
        self.assertIsInstance(instt, FileStorage)

    def test_all(self):
        instt.all() = obj
        self.assertIsInstance(obj, dict)

    def test_new(self):
        self.instt.new() = __objects
        for key in self.__objects.items():
            self.assertEqual(key, f"{self.__class__.__name__}.{self.id}")

    def test_save(self):
        self.instt.name = "task5"
        self.instt.save()
        __objects = self.instt.all()
        self.assertIn(f"{self.__class__.__name__}.{self.id}", __objects)

    def test_save2(self):
        self.instt.save()
        self.storage.all()

