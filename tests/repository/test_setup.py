import os
import unittest
from box import version
from box.python import ObjectFinder

class SetupTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_repository_path()
        self.finder = ObjectFinder()

    def test(self):
        package = self.finder.find(
            'package', 'setup.py', self.basedir,
            reducers=[lambda objects: list(objects)[0]])
        self.assertEqual(package['name'], 'box')
        self.assertEqual(package['version'], version)
        
    #Protected
    
    def _get_repository_path(self, *args):
        return os.path.join(os.path.dirname(__file__), '..', '..')