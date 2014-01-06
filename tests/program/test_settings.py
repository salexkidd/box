import unittest
from lib31.program.settings import Settings

class SettingsTest(unittest.TestCase):

    #Public

    def setUp(self):
        MockSettings = self._make_mock_settings_class()
        self.settings = MockSettings()
        
    def test(self):
        self.assertEqual(self.settings, {'name': 'value'})
        
    #Protected
    
    def _make_mock_settings_class(self):
        class MockSettings(Settings):
            #Public
            name = 'value'
        return MockSettings