import unittest
from box.itertools.not_emitted import NotEmitted


class NotEmittedTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(NotEmitted, Exception))
