import os
import unittest
from lib31.python import ObjectLoader

class FinderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.loader = ObjectLoader()
        self.base_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        
    def test_load(self):
        objects = self.loader.load(self.base_dir, 'module.py')
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0].__name__, 'Attribute1')
        self.assertEqual(objects[1].__name__, 'Attribute2')