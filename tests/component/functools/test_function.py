import unittest
from box.functools.function import Function

class FunctionTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.function = self._make_mock_function()

    def test(self):
        self.assertEqual(self.function('arg'), 'arg')
    
    #Protected
    
    def _make_mock_function(self):
        class mock_function(Function):
            #Public
            def __init__(self, arg):
                self._arg = arg
            def __call__(self):
                return self._arg
        return mock_function