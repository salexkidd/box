import unittest
from io import StringIO
from unittest.mock import patch
from box.argparse.parser import Parser

class ParserTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.stderr = patch('sys.stderr', new_callable=StringIO).start()
        self.addCleanup(patch.stopall)
    
    def test_error(self):
        parser = Parser()
        self.assertRaises(SystemExit, parser.error, 'message')
        
    def test_error_with_exception(self):
        parser = Parser(exception=RuntimeError)
        self.assertRaises(RuntimeError, parser.error, 'message')
        self.assertFalse(self.stderr.getvalue())        