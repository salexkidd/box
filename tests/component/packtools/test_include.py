import unittest
from unittest.mock import Mock
from box.packtools.include import include

class include_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.callable = Mock()
        self.callable= include(self.callable)

    def test(self):
        self.assertTrue(getattr(self.callable, include.attribute_name))