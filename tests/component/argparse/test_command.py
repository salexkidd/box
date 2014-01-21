import unittest
from functools import partial
from unittest.mock import Mock, call
from box.argparse.command import (Command, SilentArgumentParser, 
                                  SilentArgumentParserException)

class CommandTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.MockCommand = self._make_mock_command_class()
        self.argv = ['prog', 'argument']
        self.config = {
            'prog': 'prog', 
            'arguments': [
                {'name': 'name', 'kwarg': 'kwarg'},
                {'flags': ['flag'], 'kwarg': 'kwarg'}]}
        self.partial_command = partial(self.MockCommand, 
            self.argv, config=self.config)
        self.command = self.partial_command()
        
    def test___getattr__(self):
        self.assertEqual(self.command.strip, 'namespace'.strip)
        
    def test___getattr___underscore_attribute(self):
        self.assertRaises(AttributeError, 
            getattr, self.command, '_underscore_attribute')        
    
    def test_program_help(self):
        self.assertEqual(self.command.program_help, 'program_help')
    
    def test__namespace(self):
        self.assertEqual(self.command._namespace, 'namespace')
        self.command._parser_class.return_value.parse_args(['argument'])
    
    def test__parser(self):
        self.assertEqual(self.command._parser,
                         self.command._parser_class.return_value)
        self.command._parser_class.return_value.add_argument.assert_has_calls([
            call('name', kwarg='kwarg'),
            call('flag', kwarg='kwarg')])
        
    def test__parser_bad_argument(self):
        command = self.partial_command(config={'arguments': [{}]})
        self.assertRaises(ValueError, getattr, command, '_parser')          
    
    def test__parser_arguments(self):
        self.assertEqual(self.command._parser_arguments, 
                         self.config['arguments'])
        
    def test__parser_config(self):
        self.assertEqual(self.command._parser_config, {'prog': 'prog'})
          
    def test__config_default(self):
        command = self.partial_command(config=None)
        self.assertEqual(command._config, 'default_config')        
    
    #Protected
    
    def _make_mock_command_class(self):
        class MockCommand(Command):
            #Public
            default_config = 'default_config'
            #Protected
            _parser_class = Mock(return_value=Mock(
                add_argument=Mock(),
                parse_args=Mock(return_value='namespace'),
                format_help=Mock(return_value=Mock(
                    strip=Mock(return_value='program_help')))))
        return MockCommand
    

class SilentParserTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.parser = SilentArgumentParser()

    def test_error(self):
        self.assertRaises(SilentArgumentParserException, 
                          self.parser.error, 'message')