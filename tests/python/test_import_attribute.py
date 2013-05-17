import os
import unittest
from lib31.python import import_attribute

class ImportModuleTest(unittest.TestCase):
    
    def setUp(self):
        self._path = os.path.join(os.path.dirname(__file__), 'folder')
    
    def test_import_attribute_absolute(self):
        self.assertEqual(
            import_attribute('unittest.TestCase'), 
            unittest.TestCase,
        )
        
    def test_import_attribute_relative(self):
        self.assertEqual(
            import_attribute('.module.attr', self._path), 
            'attr',
        )
        
    def test_import_attribute_bad_name(self):
        self.assertRaises(TypeError, import_attribute, '.module')        