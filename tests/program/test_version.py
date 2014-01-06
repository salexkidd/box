import unittest
from lib31.program.version import Version

class VersionTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.version = Version()