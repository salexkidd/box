import os
import unittest
from unittest.mock import patch
from box.os.enhanced_join import enhanced_join

class enhanced_join_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        patch('os.path.sep', new='/').start()  
        self.addCleanup(patch.stopall)
        self.error = os.error()

    def test(self):
        self.assertEqual(enhanced_join('x', 'y'), 'x/y')
        
    def test_with_none(self):
        self.assertEqual(enhanced_join('x', None), 'x')
    
    def test_with_error(self):
        self.assertRaises(Exception, enhanced_join) 
        
    def test_with_error_and_fallback(self):
        self.assertEqual(enhanced_join(fallback='fallback'), 'fallback')             