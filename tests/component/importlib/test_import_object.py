import unittest
from unittest.mock import Mock
from box.importlib.import_object import import_object

class import_object_Test(unittest.TestCase):

    #Public

    def test_with_name(self):
        self.assertIs(import_object('unittest.mock.Mock'), Mock)
    
    def test_with_name_in_bad_format(self):
        self.assertRaises(ValueError, 
            import_object, 'unittest')
        
    def test_with_name_for_no_object(self):
        self.assertRaises(AttributeError, 
            import_object, 'unittest.mock.no_object')
        
    def test_with_name_is_object(self):
        self.assertIs(import_object(Mock), Mock)         