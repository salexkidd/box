import box
import unittest
from packgram.tests import SetupTest

@unittest.skip('works with new packgram')
class SetupTest(SetupTest):

    #Public

    __test__ = True
        
    #Protected
    
    _package = box