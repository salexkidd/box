import unittest
from importlib import import_module
component = import_module('box.importlib.check')


class check_module_Test(unittest.TestCase):

    # Tests

    def test_module_is_available(self):
        self.assertTrue(component.check_module('unittest'))

    def test_module_is_not_available(self):
        self.assertFalse(component.check_module('not_available'))
