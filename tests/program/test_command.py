import unittest
from lib31.program.command import (SilentArgumentParser, 
                                   SilentArgumentParserException)

class CommandTest(unittest.TestCase):
    
    #Public
    
    def test(self):
        pass
    

class SilentParserTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.parser = SilentArgumentParser()

    def test_error(self):
        self.assertRaises(SilentArgumentParserException, 
                          self.parser.error, 'message')