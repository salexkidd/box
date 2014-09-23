import unittest
from unittest.mock import patch
from importlib import import_module
component = import_module('box.argparse.program')


class ProgramTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.program = self.make_mock_program()
        self.result = self.program(['program', 'argument', '-f'])

    # Helpers

    def make_mock_program(self):
        class Program(component.Program):
            # Public
            default_config = {
                'arguments': [
                    {'name': 'arguments', 'nargs': '*'},
                    {'dest': 'flags', 'flags': ['-f'], 'action': 'store_true'}]}
            def __call__(self):
                return self
        return Program

    # Tests

    def test_arguments(self):
        self.assertEqual(self.result.arguments, ['argument'])

    def test_flags(self):
        self.assertEqual(self.result.flags, True)

    def test_not_existent(self):
        self.assertRaises(AttributeError, getattr, self.result, 'not_existent')

    @patch.object(component.sys, 'argv', ['program'])
    def test_without_argv(self):
        self.result = self.program()
        self.assertEqual(self.result.arguments, [])
        self.assertEqual(self.result.flags, False)

    def test_with_bad_flag(self):
        self.result = self.program(['program', '--bad-flag'])
        self.assertRaises(SystemExit, getattr, self.result, 'arguments')

    def test_with_bad_flag_and_exception(self):
        self.result = self.program(
            ['program', '--bad-flag'], exception=ValueError)
        self.assertRaises(ValueError, getattr, self.result, 'arguments')
