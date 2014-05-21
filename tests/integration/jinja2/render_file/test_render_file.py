import os
import unittest
from functools import partial
from box.jinja2 import render_file

class render_file_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        Context = self._make_mock_context_class()
        self.prender = partial(render_file, context=Context())
        
    def test(self):
        self.assertEqual(self.prender(self._make_path('file')), 'value1')
        
    #Protected
    
    def _make_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)
    
    def _make_mock_context_class(self):
        class MockContext:
            attr1 = 'value1'
            attr2 = 'value2'
        return MockContext