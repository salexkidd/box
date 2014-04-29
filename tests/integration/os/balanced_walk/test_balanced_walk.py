import os
import unittest
from box.os import balanced_walk

class balanced_walk_Test(unittest.TestCase):

    #Public

    def test(self):
        print(list(balanced_walk(self._get_fixtures_path())))
        
    #Protected
    
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)   