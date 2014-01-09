import unittest
from box.program.version import Version

class VersionTest(unittest.TestCase):

    #Public

    def setUp(self):
        MockVersion = self._make_mock_version_class()
        self.version = MockVersion()
        
    def test(self):
        self.assertEqual(self.version, '1.0.0')
        
    def test_tuple(self):
        self.assertEqual(self.version.info, (1, 0, 0, 'final', 0))
     
    #Protected
    
    def _make_mock_version_class(self, version_level='final'):
        class MockVersion(Version):
            #Public
            major = 1
            level = version_level
        return MockVersion
    
    
class VersionTest_with_level_is_not_final(VersionTest):
    
    #Public
    
    def setUp(self):
        MockVersion = self._make_mock_version_class('candidate')
        self.version = MockVersion()
        
    def test(self):
        self.assertEqual(self.version, '1.0.0.candidate')
        
    def test_tuple(self):
        self.assertEqual(self.version.info, (1, 0, 0, 'candidate', 0))