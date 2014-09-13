import unittest
from box.importlib.check import check_module


class check_module_Test(unittest.TestCase):

    # Public

    def test_module_is_available(self):
        self.assertTrue(check_module('unittest'))

    def test_module_is_not_available(self):
        self.assertFalse(check_module('not_available'))
