import unittest
from unittest.mock import Mock
from box.importlib.import_object import import_object

class import_object_Test(unittest.TestCase):

    #Public

    def test(self):
        self.assertIs(import_object('unittest.mock.Mock'), Mock)
        
    def test_forwarding(self):
        self.assertIs(Mock, Mock)        
        
    def test_no_object(self):
        self.assertRaises(AttributeError, 
            import_object, 'unittest.mock.no_object')        