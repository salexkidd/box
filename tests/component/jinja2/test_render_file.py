import unittest
from unittest.mock import Mock, mock_open
from box.jinja2.render_file import RenderFile

class RenderFileTaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.template = Mock(render=Mock(return_value='text'))
        self.render_file = self._make_mock_render_file_function(self.template)
        self.source = '/source'
        self.target = '/target'
        
    def test_complete(self):
        self.render_file(self.source, self.target)
        self.render_file._open_function.assert_called_with(self.target, 'w')
        self.render_file._open_function().write.assert_called_with('text')
        
    def test__get_template(self):
        self.assertEqual(self.render_file._get_template(self.source), self.template)
        self.render_file._file_system_loader_class.assert_called_with('/')
        self.render_file._environment_class.assert_called_with(loader='loader')
        self.assertEqual(
            self.render_file._environment_class.return_value.template_class,
            self.render_file._module_template_class)
        (self.render_file._environment_class.return_value.get_template.
            assert_called_with('source'))
        
    def test__get_context_from_dict(self):
        context = dict()
        self.assertEqual(self.render_file._get_context(context), context)
        
    def test__get_context_from_object(self):
        context = object()
        self.assertEqual(self.render_file._get_context(context), 'context')
        self.render_file._object_context_class.assert_called_with(context)   
    
    #Protected
    
    def _make_mock_render_file_function(self, template):
        class MockRenderFile(RenderFile):
            #Public
            meta_module = 'module'
            #Protected
            _object_context_class = Mock(return_value='context')
            _open_function = mock_open()
            _environment_class = Mock(return_value=Mock(
                get_template=Mock(return_value=template)))
            _file_system_loader_class = Mock(return_value='loader')
            _object_template_class = Mock()
        mock_render_file = MockRenderFile()
        return mock_render_file