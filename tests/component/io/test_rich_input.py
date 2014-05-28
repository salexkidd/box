import unittest
from functools import partial
from unittest.mock import Mock
from box.io.rich_input import rich_input

class rich_input_Test(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.pinput = partial(rich_input, 'prompt')
    
    def test(self):
        mock_input = Mock(return_value='input')
        result = self.pinput(
            input=mock_input)
        self.assertEqual(result, 'input')
        mock_input.assert_called_with('prompt: ')
        
    def test_with_default(self):
        mock_input = Mock(return_value='')
        result = self.pinput(
            default='default', 
            input=mock_input)
        self.assertEqual(result, 'default')
        mock_input.assert_called_with('prompt (default): ')
    
    def test_with_options(self):
        mock_input = Mock(return_value='')
        mock_print = Mock()
        self.assertRaises(ValueError, 
            self.pinput, 
            options=['y', 'n'], 
            input=mock_input,
            print=mock_print)
        mock_input.assert_called_with('prompt (y/n): ')
        mock_print.assert_called_with('Try again..')
        
    def test_with_default_and_options(self):
        mock_input = Mock(return_value='')
        result = self.pinput(
            default='y',
            options=['y', 'n'], 
            input=mock_input)
        self.assertEqual(result, 'y')
        mock_input.assert_called_with('prompt ([y]/n): ')