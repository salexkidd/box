import unittest
from unittest.mock import Mock, mock_open
from box.jinja2.render_file import RenderFile

class RenderFileTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.template = Mock(render=Mock(return_value='text'))
        self.render = self._make_mock_render_file_function(self.template)
        
    def test___call__(self):
        self.assertEqual(self.render('/dirpath/filename'), 'text')
        self.render._file_system_loader_class.assert_called_with('/dirpath')
        self.render._environment_class.assert_called_with(loader='loader')
        (self.render._environment_class.return_value.get_template.
            assert_called_with('filename'))
        self.template.render.assert_called_with({})
    
    def test___call___with_target(self):
        self.assertEqual(self.render('/path', target='/target'), 'text')
        self.render._open_function.assert_called_with('/target', 'w')
        self.render._open_function().write.assert_called_with('text')
        
    def test___call___with_context_is_object(self):
        context = object()
        self.assertEqual(self.render('/path', context), 'text')
        self.render._object_context_class.assert_called_with(context)
        self.template.render.assert_called_with('object_context')   
    
    #Protected
    
    def _make_mock_render_file_function(self, template):
        class MockRenderFile(RenderFile):
            #Public
            meta_module = 'module'
            #Protected
            _object_context_class = Mock(return_value='object_context')
            _open_function = mock_open()
            _environment_class = Mock(return_value=Mock(
                get_template=Mock(return_value=template)))
            _file_system_loader_class = Mock(return_value='loader')
            _object_template_class = Mock()
        mock_render_file = MockRenderFile()
        return mock_render_file