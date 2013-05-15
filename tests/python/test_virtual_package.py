import os
import unittest
from lib31.python import VirtualPackage

class VirtualPackageTest(unittest.TestCase):  
    
    #Public
    
    def setUp(self):
        self._path = os.path.join(os.path.dirname(__file__), 'package')
        self._package = VirtualPackage(self._path)

    def test_name(self):
        pass
        
    def test_path(self):
        self.assertEqual(
            self._package.__path__,
            os.path.abspath(self._path),
        )

    def test_file(self):
        self.assertEqual(
            self._package.__file__,
            None,
        )