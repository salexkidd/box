import unittest
from functools import partial
from unittest.mock import Mock
from box.input.input import InputCall

class InputCallTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.partial_call = partial(InputCall, 'prompt')
    
    def test_execute(self):
        input_function = Mock(return_value='input')
        call = self.partial_call(
            input_function=input_function)
        self.assertEqual(call.execute(), 'input')
        input_function.assert_called_with('prompt:')
        
    def test_execute_with_default(self):
        input_function = Mock(return_value='')
        call = self.partial_call(
            default='default', 
            input_function=input_function)
        self.assertEqual(call.execute(), 'default')
        input_function.assert_called_with('prompt [default]:')
    
    def test_execute_with_options(self):
        input_function = Mock(return_value='')
        print_function = Mock()
        call = self.partial_call(
            options=['y', 'n'], 
            input_function=input_function,
            print_function=print_function)
        self.assertRaises(ValueError, call.execute)
        input_function.assert_called_with('prompt [y/n]:')
        print_function.assert_called_with('Try again..')
        
    def test_execute_with_default_and_options(self):
        input_function = Mock(return_value='')
        call = self.partial_call(
            default='y',
            options=['y', 'n'], 
            input_function=input_function)
        self.assertEqual(call.execute(), 'y')
        input_function.assert_called_with('prompt [Y/n]:')