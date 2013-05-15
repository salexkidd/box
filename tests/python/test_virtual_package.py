import os
import unittest
from lib31.python import VirtualPackage

class VirtualPackageTest(unittest.TestCase):  
    
    #Public
    
    def setUp(self):
        self._path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'package')
        )
        self._package = VirtualPackage(self._path)

    def test_repr(self):
        self.assertRegex(
            repr(self._package), 
            "^<.*>$",
        ) 

    def test_name(self):
        self.assertRegex(
            self._package.__name__, 
            'virtual_package_[a-z0-9]{32}',
        )
        
    def test_path(self):
        self.assertEqual(
            [self._path], 
            self._package.__path__,
        )