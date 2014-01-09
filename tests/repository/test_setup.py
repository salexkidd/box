import unittest
from setup import package

class SetupTest(unittest.TestCase):

    #Public

    def test(self):
        self.assertEqual(package['version'], '')