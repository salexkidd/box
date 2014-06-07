import re
import unittest
from unittest.mock import Mock
from box.findtools.filepath import FilepathMapper

class FilepathMapperTest_match(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filepath='filepath')
    
    def test___call__(self):
        #Non regex patterns - not skip always
        mapper = FilepathMapper('x*')
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)
          
    def test___call___with_filepath_is_regex(self):
        mapper = FilepathMapper(re.compile('f.*'))
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)
        

class FilepathMapperTest_not_match(FilepathMapperTest_match):

    #Public
          
    def test___call___with_filepath_is_regex(self):
        mapper = FilepathMapper(re.compile('x.*'))
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.call_count)        