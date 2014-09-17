import unittest
from importlib import import_module
component = import_module('box.package.version')


class VersionTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.version = component.Version(major=1)

    # Tests

    def test(self):
        self.assertEqual(self.version, '1.0.0')

    def test_with_base_version(self):
        self.version = component.Version(version=self.version, minor=1)
        self.assertEqual(self.version, '1.1.0')

    def test_with_level_is_not_final(self):
        self.version = component.Version(major=1, level='not_final')
        self.assertEqual(self.version, '1.0.0.not_final')

    def test_info(self):
        self.assertEqual(self.version.info, (1, 0, 0, 'final', 0))
