import os
import unittest
from lib31.python import ObjectLoader

class FinderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.loader = ObjectLoader()
        
    def test_load(self):
        objects = self.loader.load(self._get_path(), 'module.py')
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0].__name__, 'Attribute1')
        self.assertEqual(objects[1].__name__, 'Attribute2')        
        
    def test__find_files(self):
        files = self.loader._find_files(self._get_path(), 'module.py')
        self.assertEqual(len(files), 2)
        self.assertEqual(files[0], self._get_path('module.py'))
        self.assertEqual(files[1], self._get_path('folder', 'module.py'))
        
    def test__import_modules(self):
        files = self.loader._find_files(self._get_path(), 'module.py')
        modules = self.loader._import_modules(files)
        self.assertEqual(len(modules), 2)
        self.assertNotEqual(modules[0], modules[1])

    def test__get_objects(self):
        files = self.loader._find_files(self._get_path(), 'module.py')
        modules = self.loader._import_modules(files)
        objects = self.loader._get_objects(modules)     
        self.assertEqual(len(objects), 2)
        self.assertNotEqual(objects[0], objects[1])
        
    #Protected
    
    def _get_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)