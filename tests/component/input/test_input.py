import unittest
from functools import partial
from unittest.mock import Mock
from box.input.input import InputCall

class InputCallTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.call_constructor = partial(InputCall, 'prompt')
    
    def test___call__(self):
        input_function = Mock(return_value='input')
        call = self.call_constructor(input_function=input_function)
        self.assertEqual(call(), 'input')
        input_function.assert_called_with('prompt')
        
    def test___call___with_default(self):
        input_function = Mock(return_value='')
        call = self.call_constructor(
            default='default', input_function=input_function)
        self.assertEqual(call(), 'default')
    
    def test___call___with_options(self):
        input_function = Mock(return_value='')
        print_function = Mock()
        call = self.call_constructor(options=['option'], 
            input_function=input_function,
            print_function=print_function)
        self.assertRaises(ValueError, call)
        print_function.assert_called_with('Try again..')