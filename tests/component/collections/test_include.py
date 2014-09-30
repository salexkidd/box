import unittest
from importlib import import_module
component = import_module('box.collections.include')


class include_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.function = component.include(self.function)

    # Helpers

    @staticmethod
    def function(self):
        pass

    # Tests

    def test(self):
        self.assertTrue(getattr(self.function, component.include.marker))
