import unittest
from importlib import import_module
component = import_module('box.statement.raise_')


class raise_exception_Test(unittest.TestCase):

    # Tests

    def test(self):
        self.assertRaises(Exception, component.raise_, Exception())
