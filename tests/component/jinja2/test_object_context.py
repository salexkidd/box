import unittest
from unittest.mock import Mock
from box.jinja2.object_context import ObjectContext

class ObjectContextTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.object = Mock(key='value', spec=['key'])
        self.context = ObjectContext(self.object)
        
    def test___contains__(self):
        self.assertTrue('key' in self.context)
    
    def test___getitem__(self):
        self.assertEqual(self.context['key'], 'value')
    
    def test___getitem___key_error(self):
        self.assertRaises(KeyError, self.context.__getitem__, 'no_key')