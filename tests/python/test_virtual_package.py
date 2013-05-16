import os
import unittest
import importlib
from lib31.python import VirtualPackage

class VirtualPackageTest(unittest.TestCase):  
    
    #Public
    
    def setUp(self):
        self._path = os.path.abspath('test."!path')
        self._package = VirtualPackage(self._path)

    def test_import(self):
        self.assertEqual(
            importlib.import_module(self._package.__name__), 
            self._package,
        )        

    def test_repr(self):
        self.assertRegex(
            repr(self._package), 
            "^<.*>$",
        ) 

    def test_name(self):
        self.assertNotIn(
            '.',                         
            self._package.__name__, 
        )
        
    def test_path(self):
        self.assertEqual(
            self._package.__path__,
            [self._path],             
        )