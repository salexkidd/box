import unittest
from box.logging.settings import Settings

class SettingsTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.Settings = self._make_mock_settings_class()
        self.settings = self.Settings()
    
    def test_argparse(self):
        self.assertEqual(self.settings.argparse['prog'], 'prog')
        
    def test_logging(self):
        self.assertEqual(self.settings.logging['handlers']['default']['level'],
            'WARNING')
    
    #Protected
    
    def _make_mock_settings_class(self):
        class MockSetting(Settings):
            #Public
            @property
            def argparse(self):
                return self._inherit_argparse(MockSetting, 
                    {'prog': 'prog'})
            @property
            def logging(self):
                return self._inherit_logging(MockSetting, 
                    {'handlers': {'default': {'level': 'WARNING'}}})               
        return MockSetting   