import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('box.argparse.program')


class ProgramTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.argv = ['prog', 'argument', '-f']
        self.config = {
            'prog': 'prog',
            'arguments': [
                {'name': 'arguments', 'nargs': '*'},
                {'dest': 'flags', 'flags': ['-f'], 'action': 'store_true'}]}
        self.Program = self.make_mock_program_class()
        self.program = self.Program(self.argv, config=self.config)

    # Helpers

    def make_mock_program_class(self):
        class MockProgram(component.Program):
            # Public
            __call__ = Mock()
        return MockProgram

    # Tests

    def test_arguments(self):
        self.assertEqual(self.program.arguments, ['argument'])

    def test_flags(self):
        self.assertEqual(self.program.flags, True)

    def test_not_existen(self):
        self.assertRaises(AttributeError, getattr, self.program, 'not_existen')

#     # Actions
#
#     def setUp(self):
#         self.stderr = patch('sys.stderr', new_callable=StringIO).start()
#         self.addCleanup(patch.stopall)
#
#     # Tests
#
#     def test_error(self):
#         parser = component.Parser()
#         self.assertRaises(SystemExit, parser.error, 'message')
#
#     def test_error_with_exception(self):
#         parser = component.Parser(exception=RuntimeError)
#         self.assertRaises(RuntimeError, parser.error, 'message')
#         self.assertFalse(self.stderr.getvalue())
