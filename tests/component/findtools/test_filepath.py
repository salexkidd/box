import re
import unittest
from unittest.mock import Mock
from box.findtools.filepath import FilepathMapper

class FilepathMapperTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filepath='filepath')
    
    def test___call__(self):
        #Non regex patterns - not skip always
        mapper = FilepathMapper('x*')
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)
          
    def test___call___with_filepath_is_regex(self):
        #Pattern matchs - not skip
        mapper = FilepathMapper(re.compile('f.*'))
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)
        #Pattern doesn't match - skip
        mapper = FilepathMapper(re.compile('x.*'))
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.call_count)