import unittest
from lib31.program.command import (SilentArgumentParser, 
                                   SilentArgumentParserException)

class SilentParserTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.parser = SilentArgumentParser()

    def test_error(self):
        self.assertRaises(SilentArgumentParserException, 
                          self.parser.error, 'message')