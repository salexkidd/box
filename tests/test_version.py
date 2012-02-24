import unittest
from pprint import pprint
from lib31.version import Version

class VersionTest(unittest.TestCase):
    
    def setUp(self):
        self.version = Version()
        
    def test(self):
        pprint(self.version.info)
        pprint(self.version.path)
        pprint(self.version.code)
        pprint(self.version.next())