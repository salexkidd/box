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
                return (self.arguments, self.flags)
        return program

    # Tests

    def test(self):
        result = self.program(['program'])
        self.assertEqual(result, ([], False))

    def test_with_arguments(self):
        result = self.program(['program', 'argument'])
        self.assertEqual(result, (['argument'], False))

    def test_with_arguments_and_flags(self):
        result = self.program(['program', 'argument', '-f'])
        self.assertEqual(result, (['argument'], True))
