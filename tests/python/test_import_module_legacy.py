import os
import unittest
from lib31.python import import_module

class ImportModuleTest(unittest.TestCase):
    
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.path = [os.path.join(dirname, 'package')]
    
    def test_import_module(self):
        self.assertEqual(
            import_module('unittest'), 
            import_module(unittest),
            unittest,
        )
        
    def test_import_attr(self):
        self.assertEqual(
            import_module('unittest.TestCase'), 
            import_module(unittest.TestCase),
            unittest.TestCase,
        )
        
    def test_import_module_with_path(self):
        self.assertRaises(
            ImportError, 
            import_module, 
            'unittest', 
            path=self.path,
        )

    def test_import_attr_with_path(self):
        self.assertRaises(
            ImportError,
            import_module,
            'unittest.TestCase', 
            path=self.path,
        )

    def test_import_module_from_path_with_path(self):
        self.assertEqual(
            import_module('module', path=self.path).attr, 
            'attr'
        )
        
    def test_import_attr_from_path_with_path(self):        
        self.assertEqual(
            import_module('module.attr', path=self.path), 
            'attr'
        )                