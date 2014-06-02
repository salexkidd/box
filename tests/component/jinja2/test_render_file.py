from box.importlib import check_module

if check_module('jinja2'):
    import unittest
    from functools import partial
    from unittest.mock import Mock, mock_open
    from box.jinja2.render_file import render_file
    
    class render_file_Test(unittest.TestCase):
    
        #Public
    
        def setUp(self):
            self.template = Mock(render=Mock(return_value='text'))
            self.render = self._make_mock_render(self.template)
            self.prender = partial(self.render, '/dirpath/filename')
            
        def test(self):
            result = self.prender()
            self.assertEqual(result, 'text')
            self.render._file_system_loader_class.assert_called_with('/dirpath')
            self.render._environment_class.assert_called_with(loader='loader')
            (self.render._environment_class.  
                return_value.get_template.assert_called_with('filename'))
            self.template.render.assert_called_with({})
        
        def test_with_target(self):
            result = self.prender(target='/target')
            self.assertEqual(result, None)
            self.render._open.assert_called_with('/target', 'w')
            self.render._open().write.assert_called_with('text')
            
        def test_with_context_is_object(self):
            context = object()
            result = self.prender(context)
            self.assertEqual(result, 'text')
            self.template.render.assert_called_with(context)   
        
        #Protected
        
        def _make_mock_render(self, template):
            class mock_render(render_file):
                #Public
                meta_module = 'module'
                #Protected
                _open = mock_open()
                _file_system_loader_class = Mock(return_value='loader')            
                _environment_class = Mock(return_value=Mock(
                    get_template=Mock(return_value=template)))
            return mock_render           