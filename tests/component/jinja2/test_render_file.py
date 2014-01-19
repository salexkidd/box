import unittest
from functools import partial
from unittest.mock import Mock, mock_open
from box.jinja2.render_file import RenderFileCall

class RenderFileCallTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.template = Mock(render=Mock(return_value='text'))
        MockCall = (self._make_mock_call_class(self.template))
        self.partial_call = partial(MockCall, '/dirpath/filename')
        
    def test_execute(self):
        call = self.partial_call()
        self.assertEqual(call.execute(), 'text')
        call._file_system_loader_class.assert_called_with('/dirpath')
        call._environment_class.assert_called_with(loader='loader')
        (call._environment_class.return_value.get_template.
            assert_called_with('filename'))
        self.template.render.assert_called_with({})
    
    def test_execute_with_target(self):
        call = self.partial_call(target='/target')
        self.assertEqual(call.execute(), 'text')
        call._open_function.assert_called_with('/target', 'w')
        call._open_function().write.assert_called_with('text')
        
    def test_execute_with_context_is_object(self):
        context = object()
        call = self.partial_call(context) 
        self.assertEqual(call.execute(), 'text')
        call._object_context_class.assert_called_with(context)
        self.template.render.assert_called_with('object_context')   
    
    #Protected
    
    def _make_mock_call_class(self, template):
        class MockCall(RenderFileCall):
            #Public
            meta_module = 'module'
            #Protected
            _object_context_class = Mock(return_value='object_context')
            _open_function = mock_open()
            _environment_class = Mock(return_value=Mock(
                get_template=Mock(return_value=template)))
            _file_system_loader_class = Mock(return_value='loader')
            _object_template_class = Mock()
        return MockCall