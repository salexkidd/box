import os
import unittest
from box import Settings

class SettingsTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.Settings = self._make_mock_settings()

    def test(self):
        settings = self.Settings()
        self.assertEqual(settings.attr, 'attr')
    
    #Protected
    
    def _make_mock_settings(self):
        class MockSettings(Settings):
            attr='attr'
        return MockSettings
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)  