import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('box.argparse.program')


class ProgramTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.argv = ['prog', 'argument']
        self.Program = self.make_mock_program_class()
        self.program = self.Program(self.argv)

    # Helpers

    def make_mock_program_class(self):
        class MockProgram(component.Program):
            # Public
            __call__ = Mock()
        return MockProgram

    # Tests

    @patch('box.argparse.program.Program._Command')
    @patch('box.argparse.program.Program._Settings')
    def test__command(self, Settings, Command):
        self.assertEqual(self.program._command, Command.return_value)
        Settings.assert_called_with()
        Command.assert_called_with(
            self.argv, config=Settings.return_value.argparse)
