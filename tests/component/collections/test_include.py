import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('box.collections.include')


class include_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.method = Mock()
        self.method = component.include(self.method)

    # Tests

    def test(self):
        self.assertTrue(getattr(self.method, component.include.attribute_name))
