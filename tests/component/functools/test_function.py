import unittest
from box.functools.function import Function

class FunctionTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.function = self._make_mock_function()

    def test(self):
        self.assertEqual(self.function('arg'), 'arg')

    def test_isinstance(self):
        self.assertIsInstance(self.function, Function)
        self.assertIsInstance(self.function, type(Function))
        # Python doesn't call __instancecheck__ on most of isinstance
        # calls but we have to test instance check inheritance
        self.assertFalse(self.function.__instancecheck__(Exception))

    # Protected

    def _make_mock_function(self):
        class mock_function(Function):
            # Public
            def __init__(self, arg):
                self._arg = arg
            def __call__(self):
                return self._arg
        return mock_function
