import unittest
from unittest.mock import Mock
from box.itertools.getfirst import GetfirstMapper

class GetfirstMapperTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock()

    def test___call___with_getfirst_is_true(self):
        mapper = GetfirstMapper(True)
        mapper(self.emitter)
        self.emitter.stop.assert_called_with(if_not_skipped=True)
        
    def test___call___with_getfirst_is_false(self):
        mapper = GetfirstMapper(False)
        mapper(self.emitter)
        self.assertFalse(self.emitter.stop.call_count)        