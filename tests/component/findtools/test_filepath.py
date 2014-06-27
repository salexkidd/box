import re
import unittest
from unittest.mock import Mock
from box.findtools.filepath import FilepathConstraint, FilepathMapper

class FilepathMapperTest_not_skip(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filepath='filepath')
    
    def test___call__(self):
        constraint = FilepathConstraint('f*')
        mapper = FilepathMapper(constraint)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
          
    def test___call___with_filepath_is_regex(self):
        constraint = FilepathConstraint(re.compile('f.*'))
        mapper = FilepathMapper(constraint)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
        

class FilepathMapperTest_skip(FilepathMapperTest_not_skip):

    #Public   
    
    def test___call__(self):
        constraint = FilepathConstraint('x*')
        mapper = FilepathMapper(constraint)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)
            
    def test___call___with_filepath_is_regex(self):
        constraint = FilepathConstraint(re.compile('x.*'))
        mapper = FilepathMapper(constraint)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)        