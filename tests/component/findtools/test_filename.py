import re
import unittest
from unittest.mock import Mock
from box.findtools.filename import FilenameConstraint, FilenameMapper

class FilenameMapperTest_not_skip(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filename='filename')
    
    def test___call__(self):
        constraint = FilenameConstraint('f*')
        mapper = FilenameMapper(constraint)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
          
    def test___call___with_filename_is_regex(self):
        constraint = FilenameConstraint(re.compile('f.*'))
        mapper = FilenameMapper(constraint)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)


class FilenameMapperTest_skip(FilenameMapperTest_not_skip):

    #Public
    
    def test___call__(self):
        constraint = FilenameConstraint('x*')
        mapper = FilenameMapper(constraint)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)
          
    def test___call___with_filename_is_regex(self):
        constraint = FilenameConstraint(re.compile('x.*'))        
        mapper = FilenameMapper(constraint)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)