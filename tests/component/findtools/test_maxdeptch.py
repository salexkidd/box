import os
import unittest
from unittest.mock import Mock
from box.findtools.maxdepth import MaxdepthMapper

class MaxdepthMapperTest_match(unittest.TestCase):

    #Public
    
    def setUp(self):
        #Depth is 2
        self.emitter = Mock(filepath=os.path.join('file', 'path'))
    
    def test___call__(self):
        mapper = MaxdepthMapper(2)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
        self.assertFalse(self.emitter.stop.called)


class MaxdepthMapperTest_not_match(MaxdepthMapperTest_match):

    #Public
    
    def test___call__(self):
        mapper = MaxdepthMapper(1)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)
        self.assertTrue(self.emitter.stop.called)       