import os
import unittest
from box import Settings

class SettingsTest(unittest.TestCase):

    #Public

    def test(self):
        settings = self._make_mock_settings_class()()
        self.assertEqual(settings, 
            {'attr1': 'value1'})
        
    def test_extension_is_dict(self):
        extension = {'attr2': 'value2'}
        settings = self._make_mock_settings_class([extension])()
        self.assertEqual(settings, 
            {'attr1': 'value1', 
             'attr2': 'value2'})
        
    def test_extension_is_settings(self):
        extension = Settings(attr2='value2')
        settings = self._make_mock_settings_class([extension])()
        self.assertEqual(settings, 
            {'attr1': 'value1', 
             'attr2': 'value2'})
        
    def test_extension_is_path_to_file_with_settings(self):
        extension = self._get_fixtures_path('settings1.py')
        settings = self._make_mock_settings_class([extension])()
        self.assertEqual(settings, 
            {'attr1': 'value1', 
             'attr2': 'value2'}) 
        
    def test_extension_is_path_to_file_without_correct_settings(self):
        extension = self._get_fixtures_path('settings2.py')
        MockSettings = self._make_mock_settings_class([extension])
        self.assertRaises(RuntimeError, MockSettings)
    
    #Protected
    
    def _make_mock_settings_class(self, extensions=[]):
        class MockSettings(Settings):
            #Public
            attr1='value1'
            #Protected
            _extensions=extensions
        return MockSettings
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)  