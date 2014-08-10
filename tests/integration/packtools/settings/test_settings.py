import os
import unittest
from unittest.mock import Mock, ANY
from box.packaging import Settings


class SettingsTest(unittest.TestCase):

    # Public

    def tearDown(self):
        try:
            os.remove(self._make_path('settings3.py'))
        except os.error:
            pass

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

    def test_extension_is_path_to_file_with_user_settings(self):
        extension = self._make_path('settings1.py')
        settings = self._make_mock_settings_class([extension])()
        self.assertEqual(settings,
            {'attr1': 'value1',
             'attr2': 'value2'})

    def test_extension_is_path_to_without_settings_file(self):
        mock_onerror = Mock()
        extension = self._make_path('settings2.py')
        MockSettings = self._make_mock_settings_class([extension])
        MockSettings._handle_extension_error = mock_onerror
        settings = MockSettings()
        self.assertEqual(settings, {'attr1': 'value1'})
        mock_onerror.assert_called_with(extension, ANY)

    def test_extension_is_path_to_non_existent_file(self):
        extension = self._make_path('settings3.py')
        # Settings have to create non existent file
        self.assertFalse(os.path.isfile(extension))
        settings = self._make_mock_settings_class([extension])()
        self.assertEqual(settings,
            {'attr1': 'value1'})
        # Now file exists and contains user settings stub
        self.assertTrue(os.path.isfile(extension))
        settings = self._make_mock_settings_class([extension])()
        self.assertEqual(settings,
            {'attr1': 'value1'})

    # Protected

    def _make_mock_settings_class(self, extensions=[]):
        class MockSettings(Settings):
            # Public
            attr1 = 'value1'
            # Protected
            _extensions = extensions
        return MockSettings

    def _make_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)
