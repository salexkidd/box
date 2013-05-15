import os
import unittest
from lib31.python import VirtualPackage

class VirtualPackageTest(unittest.TestCase):  
    
    #Public
    
    def setUp(self):
        self._path = os.path.join(os.path.dirname(__file__), 'package')
        self._package = VirtualPackage(self._path)

    def test_name(self):
        self.assertIn(
            'virtual_package_', 
            self._package.__name__,
        )
        
    def test_path(self):
        self.assertIn(
            self._path, 
            self._package.__path__[0],
        )