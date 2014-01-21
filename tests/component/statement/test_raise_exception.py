import unittest
from box.statement.raise_exception import raise_exception

class raise_exception_Test(unittest.TestCase):

    #Public

    def test(self):
        self.assertRaises(Exception, raise_exception, Exception())