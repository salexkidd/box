import re
import unittest
from unittest.mock import Mock
from box.findtools.filename import FilenameCondition, FilenameMapper

class FilenameMapperTest_not_skip(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filename='filename')
    
    def test___call__(self):
        condition = FilenameCondition('f*')
        mapper = FilenameMapper(condition)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
          
    def test___call___with_filename_is_regex(self):
        condition = FilenameCondition(re.compile('f.*'))
        mapper = FilenameMapper(condition)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)


class FilenameMapperTest_skip(FilenameMapperTest_not_skip):

    #Public
    
    def test___call__(self):
        condition = FilenameCondition('x*')
        mapper = FilenameMapper(condition)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)
          
    def test___call___with_filename_is_regex(self):
        condition = FilenameCondition(re.compile('x.*'))        
        mapper = FilenameMapper(condition)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)