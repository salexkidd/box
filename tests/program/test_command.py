import unittest
from functools import partial
from unittest.mock import Mock
from lib31.program.command import (Command, SilentArgumentParser, 
                                   SilentArgumentParserException)

class CommandTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.MockCommand = self._make_mock_command_class()
        self.argv = ['prog', 'argument']
        self.config = {}
        self.command_constructor = partial(self.MockCommand, 
            self.argv, config=self.config)
    
    def test__namespace(self):
        command = self.command_constructor()
        self.assertEqual(command._namespace, 'namespace')
        command._parser_class.return_value.parse_args(['argument'])
        
    def test__parser(self):
        command = self.command_constructor()
        self.assertEqual(command._parser, command._parser_class.return_value)
        command._parser_class.assert_called_with(**self.config)
          
    def test__config_default(self):
        command = self.command_constructor(config=None)
        self.assertEqual(command._config, 'default_config')        
    
    #Protected
    
    def _make_mock_command_class(self):
        class MockCommand(Command):
            #Protected
            _default_config = 'default_config'
            _parser_class = Mock(return_value=Mock(
                parse_args=Mock(return_value='namespace')))
        return MockCommand
    

class SilentParserTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.parser = SilentArgumentParser()

    def test_error(self):
        self.assertRaises(SilentArgumentParserException, 
                          self.parser.error, 'message')