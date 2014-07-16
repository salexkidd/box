import unittest
from unittest.mock import Mock
from box.copy import enhanced_copy
from box.jinja2.context import ObjectContext

class ObjectContextTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.object = Mock(key1='value1', spec=['key1'])
        self.context = ObjectContext(self.object, key2='value2')

    def test___contains__(self):
        self.assertTrue('key1' in self.context)
        self.assertTrue('key2' in self.context)

    def test___getitem__(self):
        self.assertEqual(self.context['key1'], 'value1')

    def test___getitem___key_error(self):
        self.assertRaises(KeyError, self.context.__getitem__, 'no_key')

    def test___copy__(self):
        context_copy = enhanced_copy(self.context)
        self.assertEqual(context_copy['key1'], 'value1')
        self.assertEqual(context_copy['key2'], 'value2')
