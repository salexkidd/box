import os
import unittest
from operator import itemgetter
from box import version
from box.findtools import find_objects

class SetupTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_repository_path()

    def test(self):
        package = find_objects(
            objectname='package', 
            filename='setup.py', 
            basedir=self.basedir, 
            max_depth=1,
            reducers=[list, itemgetter(0)])
        self.assertEqual(package['name'], 'box')
        self.assertEqual(package['version'], version)
        
    #Protected
    
    def _get_repository_path(self, *args):
        return os.path.join(os.path.dirname(__file__), '..', '..')