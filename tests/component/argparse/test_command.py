import unittest
from functools import partial
from unittest.mock import Mock, call
from importlib import import_module
component = import_module('box.argparse.command')


class CommandTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Command = self.make_mock_command_class()
        self.argv = ['prog', 'argument']
        self.config = {
            'prog': 'prog',
            'arguments': [
                {'name': 'name', 'kwarg': 'kwarg'},
                {'flags': ['flag'], 'kwarg': 'kwarg'}]}
        self.pcommand = partial(self.Command,
            self.argv, config=self.config)
        self.command = self.pcommand()

    # Helpers

    def make_mock_command_class(self):
        class MockCommand(component.Command):
            # Protected
            _Parser = Mock(return_value=Mock(
                add_argument=Mock(),
                parse_args=Mock(return_value='namespace'),
                format_help=Mock(return_value=Mock(
                    strip=Mock(return_value='program_help')))))
        return MockCommand

    # Tests

    def test___getattr__(self):
        self.assertEqual(self.command.strip, 'namespace'.strip)

    def test___getattr___underscore_attribute(self):
        self.assertRaises(AttributeError,
            getattr, self.command, '_underscore_attribute')

    def test_program_help(self):
        self.assertEqual(self.command.program_help, 'program_help')

    def test__namespace(self):
        self.assertEqual(self.command._namespace, 'namespace')
        self.command._Parser.return_value.parse_args(['argument'])
