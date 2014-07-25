import unittest
from box.functools.null import Null

class NullTest(unittest.TestCase):

    # Public

    def test_bool(self):
        self.assertFalse(Null)

    def test_repr(self):
        self.assertEqual(repr(Null), 'Null')

    def test_isinstance(self):
        self.assertTrue(isinstance(Null, Null))