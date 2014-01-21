import unittest
from functools import partial
from unittest.mock import Mock, mock_open
from box.jinja2.render_file import render_file

class render_file_Test(unittest.TestCase):

    #Public

    def setUp(self):
        self.template = Mock(render=Mock(return_value='text'))
        self.render = self._make_mock_render_function(self.template)
        self.partial_render = partial(self.render, '/dirpath/filename')
        
    def test(self):
        result = self.partial_render()
        self.assertEqual(result, 'text')
        (self.render._call_class._file_system_loader_class.
            assert_called_with('/dirpath'))
        (self.render._call_class._environment_class.
            assert_called_with(loader='loader'))
        (self.render._call_class._environment_class.
         return_value.get_template.
            assert_called_with('filename'))
        self.template.render.assert_called_with({})
    
    def test_with_target(self):
        result = self.partial_render(target='/target')
        self.assertEqual(result, 'text')
        (self.render._call_class._open_function.
            assert_called_with('/target', 'w'))
        (self.render._call_class._open_function().write.
            assert_called_with('text'))
        
    def test_with_context_is_object(self):
        context = object()
        result = self.partial_render(context)
        self.assertEqual(result, 'text')
        (self.render._call_class._object_context_class.
            assert_called_with(context))
        self.template.render.assert_called_with('object_context')   
    
    #Protected
    
    def _make_mock_render_function(self, template):
        class MockRenderCall(render_file._call_class):
            #Public
            meta_module = 'module'
            #Protected
            _object_context_class = Mock(return_value='object_context')
            _open_function = mock_open()
            _environment_class = Mock(return_value=Mock(
                get_template=Mock(return_value=template)))
            _file_system_loader_class = Mock(return_value='loader')
            _object_template_class = Mock()
        class MockRender(type(render_file)):
            #Protected
            _call_class = MockRenderCall
        return MockRender()           