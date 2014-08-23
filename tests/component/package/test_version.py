import unittest
from box.package import Version


class VersionTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.version = Version(major=1)

    def test(self):
        self.assertEqual(self.version, '1.0.0')

    def test_with_base_version(self):
        self.version = Version(version=self.version, minor=1)
        self.assertEqual(self.version, '1.1.0')

    def test_with_level_is_not_final(self):
        self.version = Version(major=1, level='not_final')
        self.assertEqual(self.version, '1.0.0.not_final')

    def test_info(self):
        self.assertEqual(self.version.info, (1, 0, 0, 'final', 0))
