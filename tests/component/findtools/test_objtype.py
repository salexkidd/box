import unittest
from unittest.mock import Mock
from box.findtools.objtype import ObjtypeMapper

class ObjtypeMapperTest_match(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(object=ZeroDivisionError())
    
    def test___call__(self):
        mapper = ObjtypeMapper(ArithmeticError)
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)
          
    def test___call___with_objtype_is_list(self):
        mapper = ObjtypeMapper([ArithmeticError, BufferError])
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)


class ObjtypeMapperTest_not_match(ObjtypeMapperTest_match):

    #Public
    
    def test___call__(self):
        mapper = ObjtypeMapper(AssertionError)
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)
          
    def test___call___with_objtype_is_list(self):
        mapper = ObjtypeMapper([AssertionError, AttributeError])
        mapper(self.emitter)
        self.assertTrue(self.emitter.skip.called)