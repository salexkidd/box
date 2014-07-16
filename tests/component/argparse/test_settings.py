import unittest
from box.argparse.settings import Settings

class SettingsTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Settings = self._make_mock_settings_class()
        self.settings = self.Settings()

    def test(self):
        self.assertEqual(self.settings,
            {'argparse': {'prog': 'prog2', 'arguments': ['arg1', 'arg2']}})

    # Protected

    def _make_mock_settings_class(self):
        class MockSetting1(Settings):
            # Public
            @property
            def argparse(self):
                return self._inherit_argparse(MockSetting1,
                    {'prog': 'prog1', 'arguments': ['arg1']})
        class MockSetting2(MockSetting1):
            # Public
            @property
            def argparse(self):
                return self._inherit_argparse(MockSetting2,
                    {'prog': 'prog2', 'arguments': ['arg2']})
        return MockSetting2
