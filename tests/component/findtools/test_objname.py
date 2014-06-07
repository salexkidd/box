import re
import unittest
from unittest.mock import Mock
from box.findtools.objname import ObjnameMapper

class ObjnameMapperTest_match(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(objname='objname')
    
    def test___call__(self):
        mapper = ObjnameMapper('objname')
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)
          
    def test___call___with_objname_is_regex(self):
        mapper = ObjnameMapper(re.compile('o.*'))
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.call_count)


class ObjnameMapperTest_not_match(ObjnameMapperTest_match):

    #Public
    
    def test___call__(self):
        mapper = ObjnameMapper('x')
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.call_count)
          
    def test___call___with_objname_is_regex(self):
        mapper = ObjnameMapper(re.compile('x.*'))
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.call_count)