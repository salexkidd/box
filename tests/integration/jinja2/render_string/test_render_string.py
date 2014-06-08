from box.importlib import check_module

if check_module('jinja2'):
    import os
    import shutil
    import unittest
    from unittest.mock import Mock, patch
    from box.jinja2 import render_string
    
    class render_string_Test(unittest.TestCase):
    
        #Public
        
        def tearDown(self):
            try:
                shutil.rmtree(self._make_path())
            except os.error:
                pass
        
        def test(self):
            result = render_string('{{ attr1 }}')
            self.assertEqual(result, '')        
            
        def test_with_context_is_none(self):
            result = render_string('{{ attr1 }}', None)
            self.assertEqual(result, '')
              
        def test_with_context_is_dict(self):
            result = render_string('{{ attr1 }}', {'attr1': 'value1'})
            self.assertEqual(result, 'value1')

        def test_with_context_is_object(self):
            context = Mock(attr1 = 'value1')
            result = render_string('{{ attr1 }}', context)
            self.assertEqual(result, 'value1')
        
        @patch('jinja2.utils.concat')
        def test_with_error_in_rendering(self, concat):
            concat.side_effect = Exception()
            self.assertRaises(Exception, render_string, '{{ attr1 }}')
            
        def test_with_target(self):
            target=self._make_path('target')
            render_string('value1', target=target)
            with open(target) as file:
                self.assertEqual(file.read(), 'value1')
            
        #Protected
        
        def _make_path(self, *args):
            return os.path.join(os.path.dirname(__file__), 'fixtures', *args) 