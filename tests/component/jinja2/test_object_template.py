import unittest
from unittest.mock import Mock
from box.jinja2.object_template import ObjectTemplateMixin

class ObjectTemplateTest(unittest.TestCase):    
    
    #Public
    
    def test_render(self):
        template = Mock(
            new_context = Mock(return_value='new_context'),
            root_render_func=Mock(return_value='root_render'),
            _concat_operator=Mock(return_value='result'))
        self.assertEqual(ObjectTemplateMixin.render(template, 'context'), 'result')
        template.new_context.assert_called_with('context', shared=True)
        template.root_render_func.assert_called_with('new_context')
        template._concat_operator.assert_called_with('root_render')