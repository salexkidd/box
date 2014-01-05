import os
import unittest
from lib31.python import ObjectLoader

class FinderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.loader = ObjectLoader()
        self.basedir = os.path.join(os.path.dirname(__file__), 'fixtures')
      
    def test_load(self):
        objects = list(self.loader.load(self.basedir, 'module.py'))
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0].__name__, 'Attribute1')
         
    def test_load_recursively(self):
        objects = list(self.loader.load(self.basedir, 'module.py', True))
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0].__name__, 'Attribute1')
        self.assertEqual(objects[1].__name__, 'Attribute2')
        