import unittest
from importlib import import_module
component = import_module('box.argparse.settings')


class SettingsTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Settings = self.make_mock_settings_class()
        self.settings = self.Settings()

    # Helpers

    def make_mock_settings_class(self):
        class MockSetting1(component.Settings):
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

    # Tests

    def test(self):
        self.assertEqual(self.settings,
            {'argparse': {'prog': 'prog2', 'arguments': ['arg1', 'arg2']}})
