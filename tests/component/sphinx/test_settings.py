import unittest
from unittest.mock import Mock
from box.sphinx.settings import Settings

class SettingsTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.Settings = self._make_mock_settings_class()
        self.settings = self.Settings()

    def test___getattr__(self):
        self.assertEqual(self.settings.master_doc, 'master_doc')
        
    def test___getattr___non_existent(self):
        self.assertRaises(AttributeError, 
            getattr, self.settings, 'non_existent')
        
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
            project = 'project'
            version = 'version'
            #Protected
            _defaults = Mock(
                master_doc = 'master_doc',                             
                spec = ['master_doc'],
            )
        return MockSettings