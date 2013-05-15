import os
import sys
import unittest
from lib31.python import VirtualPackage

class VirtualPackageTest(unittest.TestCase):  
    
    def setUp(self):
        self.package = VirtualPackage([self.get_path('package')])
        
    def get_path(self, *paths):
        return os.path.join(os.path.dirname(__file__), *paths)
    
    def test(self):
        self.assertEqual(
            self.package, 
            sys.modules[self.package.__name__]
        )

    def test_file(self):
        print(self.package.__file__)