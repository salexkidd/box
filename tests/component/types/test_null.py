import unittest
from box.types.null import Null

class NullTest(unittest.TestCase):

    # Public

    def test_bool(self):
        self.assertFalse(Null)

    def test_repr(self):
        self.assertEqual(repr(Null), 'Null')
