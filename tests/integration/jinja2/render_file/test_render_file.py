import os
import unittest
from functools import partial
from box.jinja2 import render_file

class render_file_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        class Context:
            attr1 = 'value1'
            attr2 = 'value2'
        self.prender = partial(render_file, context=Context())
        
    def test(self):
        self.assertEqual(
            self.prender(self._make_path('template1')), 
            'value1\nvalue2')
        
    #Protected
    
    def _make_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)