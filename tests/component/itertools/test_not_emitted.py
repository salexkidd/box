import unittest
from box.itertools.not_emitted import NotEmitted

class NotEmittedTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertRaises(NotEmitted, self._raise)

    # Protected

    def _raise(self):
        raise NotEmitted()
