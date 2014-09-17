import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('box.sphinx.settings')


class SettingsTest(unittest.TestCase):

    # Actions

    def setUp(self):
        sphinx_config = Mock(attr1='value1', spec=['attr1'])
        import_module = patch('box.sphinx.settings.import_module').start()
        import_module.return_value.Config = Mock(return_value=sphinx_config)
        self.addCleanup(patch.stopall)
        self.method = Mock()
        self.Settings = self.make_mock_settings_class(self.method)
        # Passed sphinx module makes no difference
        self.settings = self.Settings(sphinx=unittest)

    # Helpers

    def make_mock_settings_class(self, method):
        class MockSettings(component.Settings):
            # Public
            author = 'author'
            master_doc = 'master_doc'
            project = 'project'
            version = 'version'
            setup_method = component.setup(method)
        return MockSettings

    # Tests

    def test___getattr__(self):
        self.assertEqual(self.settings.attr1, 'value1')
        self.assertRaises(AttributeError, getattr, self.settings, 'attr2')

    def test_release(self):
        self.assertEqual(self.settings.release, 'version')

    def test_latex_documents(self):
        self.assertEqual(self.settings.latex_documents,
            [('master_doc',
              'project.tex',
              'project Documentation',
              'author',
              'manual')])

    def test_man_pages(self):
        self.assertEqual(self.settings.man_pages,
            [('master_doc',
              'project',
              'project Documentation',
              ['author'],
              1)])

    def test_texinfo_documents(self):
        self.assertEqual(self.settings.texinfo_documents,
            [('master_doc',
              'project',
              'project Documentation',
              'author',
              'project',
              'One line description of project.',
              'Miscellaneous')])

    def test_setup(self):
        app = Mock()
        self.settings.setup(app)
        self.method.assert_called_with(self.settings, app)
