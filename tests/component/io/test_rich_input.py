import unittest
from functools import partial
from unittest.mock import Mock
from box.io.rich_input import rich_input

class rich_input_Test(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.partial_input = partial(rich_input, 'prompt')
    
    def test(self):
        input_function = Mock(return_value='input')
        result = self.partial_input(
            input_function=input_function)
        self.assertEqual(result, 'input')
        input_function.assert_called_with('prompt: ')
        
    def test_with_default(self):
        input_function = Mock(return_value='')
        result = self.partial_input(
            default='default', 
            input_function=input_function)
        self.assertEqual(result, 'default')
        input_function.assert_called_with('prompt [default]: ')
    
    def test_with_options(self):
        input_function = Mock(return_value='')
        print_function = Mock()
        self.assertRaises(ValueError, 
            self.partial_input, 
            options=['y', 'n'], 
            input_function=input_function,
            print_function=print_function)
        input_function.assert_called_with('prompt [y/n]: ')
        print_function.assert_called_with('Try again..')
        
    def test_with_default_and_options(self):
        input_function = Mock(return_value='')
        result = self.partial_input(
            default='y',
            options=['y', 'n'], 
            input_function=input_function)
        self.assertEqual(result, 'y')
        input_function.assert_called_with('prompt [Y/n]: ')