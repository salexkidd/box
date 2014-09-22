import unittest
from importlib import import_module
component = import_module('box.argparse.program')


class ProgramTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.program = self.make_mock_program()

    # Helpers

    def make_mock_program(self):
        class program(component.Program):
            # Public
            default_config = {
                'prog': 'prog',
                'arguments': [
                    {'name': 'arguments', 'nargs': '*'},
                    {'dest': 'flags', 'flags': ['-f'], 'action': 'store_true'}]}
            def __call__(self):
                return self
        return program

    # Tests

    def test(self):
        self.program = self.program(['program'])
        self.assertEqual(self.program.arguments, [])
        self.assertEqual(self.program.flags, False)

    def test_with_arguments(self):
        self.program = self.program(['program', 'argument'])
        self.assertEqual(self.program.arguments, ['argument'])
        self.assertEqual(self.program.flags, False)

    def test_with_arguments_and_flags(self):
        self.program = self.program(['program', 'argument', '-f'])
        self.assertEqual(self.program.arguments, ['argument'])
        self.assertEqual(self.program.flags, True)
