import unittest
from lib31.console import SilentParser, SilentParserException

class SilentParserTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.parser = SilentParser()

    def test_error(self):
        self.assertRaises(SilentParserException, self.parser.error, 'message')