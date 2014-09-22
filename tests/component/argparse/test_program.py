import unittest
from unittest.mock import Mock
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

    pass
