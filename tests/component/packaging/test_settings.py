import unittest
from box.packaging import Settings


class SettingsTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Settings = self._make_mock_settings_class()
        self.settings = self.Settings()

    def test(self):
        self.assertEqual(self.settings, {'name1': 'value1'})

    def test___setattr__(self):
        self.settings.name2 = 'value2'
        self.assertEqual(self.settings, {'name1': 'value1', 'name2': 'value2'})

    def test___delattr__(self):
        self.settings.name2 = 'value2'
        del self.settings.name2
        self.assertEqual(self.settings, {'name1': 'value1'})

    # Protected

    def _make_mock_settings_class(self):
        class MockSettings(Settings):
            # Public
            name1 = 'value1'
        return MockSettings
