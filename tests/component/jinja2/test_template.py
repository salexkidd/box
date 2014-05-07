import unittest
from unittest.mock import Mock, ANY
from box.jinja2.template import TemplateMixin

class TemplateMixinTest(unittest.TestCase):    
    
    #Public
    
    def setUp(self):
        MockTemplate = self._make_mock_template()
        self.template = MockTemplate()
    
    def test_render(self):
        self.assertEqual(self.template.render(None), 'result')
        self.template.new_context.assert_called_with(ANY, shared=True)
        self.template.root_render_func.assert_called_with('new_context')
        self.template._concat.assert_called_with('root_render')
        
    #Protected
    
    def _make_mock_template(self):
        class MockTemplate(TemplateMixin):
            #Public
            new_context = Mock(return_value='new_context')
            root_render_func = Mock(return_value='root_render')
            #Protected
            _concat = Mock(return_value='result')
        return MockTemplate