import unittest
from unittest.mock import Mock
from box.packtools.include import include

class include_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.method = Mock()
        self.method = include(self.method)

    def test(self):
        self.assertTrue(getattr(self.method, include.attribute_name))