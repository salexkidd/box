import unittest
from importlib import import_module
component = import_module('box.functools.function')


class FunctionTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.function = self.make_mock_function()

    # Helpers

    def make_mock_function(self):
        class mock_function(component.Function):
            # Public
            def __init__(self, arg):
                self._arg = arg
            def __call__(self):
                return self._arg
        return mock_function

    # Tests

    def test(self):
        self.assertEqual(self.function('arg'), 'arg')

    def test_isinstance(self):
        self.assertIsInstance(self.function, component.Function)
        self.assertIsInstance(self.function, type(component.Function))
        # Python doesn't call __instancecheck__ on most of isinstance
        # calls but we have to test instance check inheritance
        self.assertFalse(self.function.__instancecheck__(Exception))
