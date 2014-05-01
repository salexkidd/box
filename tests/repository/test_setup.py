import os
import unittest
from box import version
#TODO: Nose in shell imports module instead of object
from box.findtools.find_objects import find_objects

class SetupTest(unittest.TestCase):

    #Public
    
    def test(self):
        package = find_objects(
            objname='package', 
            filename='setup.py', 
            basedir=self._basedir, 
            maxdepth=1,
            getfirst=True)
        self.assertEqual(package['name'], 'box')
        self.assertEqual(package['version'], version)
        
    #Protected
    
    @property
    def _basedir(self, *args):
        return os.path.join(os.path.dirname(__file__), '..', '..')