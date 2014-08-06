import unittest
from unittest.mock import Mock, patch
from box.argparse.program import Program


class ProgramTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.argv = ['prog', 'argument']
        self.Program = self._make_mock_program_class()
        self.program = self.Program(self.argv)

    @patch('box.argparse.program.Program._Command')
    @patch('box.argparse.program.Program._Settings')
    def test__command(self, Settings, Command):
        self.assertEqual(self.program._command, Command.return_value)
        Settings.assert_called_with()
        Command.assert_called_with(
            self.argv, config=Settings.return_value.argparse)

    # Protected

    def _make_mock_program_class(self):
        class MockProgram(Program):
            # Public
            __call__ = Mock()
        return MockProgram
