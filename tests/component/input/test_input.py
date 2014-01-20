import unittest
from functools import partial
from unittest.mock import Mock
from box.input.input import InputCall

class InputCallTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.partial_call = partial(InputCall, 'prompt')
    
    def test___call__(self):
        input_function = Mock(return_value='input')
        call = self.partial_call(
            input_function=input_function)
        self.assertEqual(call.execute(), 'input')
        input_function.assert_called_with('prompt')
        
    def test___call___with_default(self):
        input_function = Mock(return_value='')
        call = self.partial_call(
            default='default', 
            input_function=input_function)
        self.assertEqual(call.execute(), 'default')
    
    def test___call___with_options(self):
        input_function = Mock(return_value='')
        print_function = Mock()
        call = self.partial_call(options=['option'], 
            input_function=input_function,
            print_function=print_function)
        self.assertRaises(ValueError, call.execute)
        print_function.assert_called_with('Try again..')