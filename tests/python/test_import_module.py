import unittest
from lib31.python import import_module

class ImportModuleTest(unittest.TestCase):
    
    def test_import_module_absolute(self):
        self.assertEqual(
            import_module('unittest'), 
            unittest,
        )
        
    def test_import_module_relative(self):
        self.assertEqual(
            import_module('.module', path='folder').attr, 
            'attr',
        )
         
    def test_import_module_relative_with_no_path(self):
        self.assertRaises(TypeError, import_module, '.module')