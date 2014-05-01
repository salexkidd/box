import os
import unittest
from box import Settings

class SettingsTest(unittest.TestCase):

    #Public

    def test(self):
        settings = self._make_mock_settings_class()()
        self.assertEqual(settings, {'attr1': 'value1'})
        
    def test_dict_extension(self):
        settings = self._make_mock_settings_class([{'attr2': 'value2'}])()
        self.assertEqual(settings, {'attr1': 'value1', 'attr2': 'value2'})         
    
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