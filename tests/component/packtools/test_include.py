import unittest
from box.packtools.include import include

class include_Test(unittest.TestCase):

    #Public

    def test(self):
        include(self)
        self.assertTrue(getattr(self, include.attribute_name))