import os
import unittest

class render_file_Test(unittest.TestCase):

    #Public

        
    #Protected
    
    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures') 