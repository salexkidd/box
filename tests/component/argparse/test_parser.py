import unittest
from io import StringIO
from unittest.mock import patch
from importlib import import_module
component = import_module('box.argparse.parser')


class ParserTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.stderr = patch('sys.stderr', new_callable=StringIO).start()
        self.addCleanup(patch.stopall)

    # Tests

    def test_error(self):
        parser = component.Parser()
        self.assertRaises(SystemExit, parser.error, 'message')

    def test_error_with_exception(self):
        parser = component.Parser(exception=RuntimeError)
        self.assertRaises(RuntimeError, parser.error, 'message')
        self.assertFalse(self.stderr.getvalue())
