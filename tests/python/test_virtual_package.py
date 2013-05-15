import os
import unittest
from lib31.python import VirtualPackage

class VirtualPackageTest(unittest.TestCase):  
    
    #Public
    
    def setUp(self):
        self._package = VirtualPackage(
            os.path.join(os.path.dirname(__file__), 'package')
        )

    def test_file(self):
        self.assertEqual(
            self._package.__file__,
            None,
        )