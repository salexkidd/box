import unittest
from box.statement.raise_ import raise_


class raise_exception_Test(unittest.TestCase):

    # Public

    def test(self):
        self.assertRaises(Exception, raise_, Exception())
