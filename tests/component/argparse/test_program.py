import unittest
from unittest.mock import Mock, patch
from box.argparse.program import Program

class ProgramTest(unittest.TestCase):

    # Public


    def setUp(self):
        self.argv = ['prog', 'argument']
        self.Program = self._make_mock_program_class()
        self.program = self.Program(self.argv)

    @patch('box.argparse.program.Program._command_class')
    @patch('box.argparse.program.Program._settings_class')
    def test__command(self, settings_class, command_class):
        self.assertEqual(self.program._command, command_class.return_value)
        settings_class.assert_called_with()
        command_class.assert_called_with(
            self.argv, config=settings_class.return_value.argparse)

    # Protected

    def _make_mock_program_class(self):
        class MockProgram(Program):
            # Public
            __call__ = Mock()
        return MockProgram
