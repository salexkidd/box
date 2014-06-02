import box
try:
    from packgram.tests import SetupTest
except ImportError:
    from unittest import TestCase as SetupTest

class SetupTest(SetupTest):

    #Public

    __test__ = True
        
    #Protected
    
    _package = box