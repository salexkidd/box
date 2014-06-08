import unittest
from box.argparse.silent import (SilentArgumentParser, 
                                  SilentArgumentParserException)

class SilentArgumentParserTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.parser = SilentArgumentParser()

    def test_error(self):
        self.assertRaises(SilentArgumentParserException, 
                          self.parser.error, 'message')