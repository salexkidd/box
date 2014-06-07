import re
import unittest
from unittest.mock import Mock
from box.findtools.filename import FilenameMapper

class FilenameMapperTest_match(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filename='filename')
    
    def test___call__(self):
        mapper = FilenameMapper('f*')
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)
          
    def test___call___with_filename_is_regex(self):
        mapper = FilenameMapper(re.compile('f.*'))
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)


class FilenameMapperTest_not_match(FilenameMapperTest_match):

    #Public
    
    def test___call__(self):
        mapper = FilenameMapper('x*')
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.call_count)
          
    def test___call___with_filename_is_regex(self):
        mapper = FilenameMapper(re.compile('x.*'))
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.call_count)