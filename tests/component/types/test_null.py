import unittest
from importlib import import_module
component = import_module('box.types.null')


class NullTest(unittest.TestCase):

    # Tests

    def test_bool(self):
        self.assertFalse(component.Null)

    def test_repr(self):
        self.assertEqual(repr(component.Null), 'Null')
