import unittest
from unittest.mock import Mock, patch
from box.sphinx.settings import Settings

class SettingsTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.Settings = self._make_mock_settings_class()
        self.settings = self.Settings()

    @patch('box.sphinx.settings.import_object')
    def test___getattr__(self, import_object):
        sphinx_config = Mock(attr1='value1', spec=['attr1'])
        import_object.return_value = Mock(return_value=sphinx_config)
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
    
    #Protected
    
    def _make_mock_settings_class(self):
        class MockSettings(Settings):
            #Public
            author = 'author'
            master_doc = 'master_doc'
            project = 'project'
            version = 'version'
        return MockSettings