import unittest
from importlib import import_module
component = import_module('box.logging.settings')


class SettingsTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Settings = self.make_mock_settings_class()
        self.settings = self.Settings()

    # Helpers

    def make_mock_settings_class(self):
        class MockSetting(component.Settings):
            # Public
            @property
            def argparse(self):
                return self._inherit_argparse(MockSetting,
                    {'prog': 'prog'})
            @property
            def logging(self):
                return self._inherit_logging(MockSetting,
                    {'handlers': {'default': {'level': 'WARNING'}}})
        return MockSetting

    # Tests

    def test_argparse(self):
        self.assertEqual(self.settings.argparse['prog'], 'prog')

    def test_logging(self):
        self.assertEqual(self.settings.logging['handlers']['default']['level'],
            'WARNING')
