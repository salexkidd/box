import re
import unittest
from unittest.mock import Mock
from box.findtools.filepath import FilepathCondition, FilepathMapper

class FilepathMapperTest_not_skip(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filepath='filepath')
    
    def test___call__(self):
        condition = FilepathCondition('f*')
        mapper = FilepathMapper(condition)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
          
    def test___call___with_filepath_is_regex(self):
        condition = FilepathCondition(re.compile('f.*'))
        mapper = FilepathMapper(condition)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
        

class FilepathMapperTest_skip(FilepathMapperTest_not_skip):

    #Public   
    
    def test___call__(self):
        condition = FilepathCondition('x*')
        mapper = FilepathMapper(condition)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)
            
    def test___call___with_filepath_is_regex(self):
        condition = FilepathCondition(re.compile('x.*'))
        mapper = FilepathMapper(condition)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)        