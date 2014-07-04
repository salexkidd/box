import re
import unittest
from unittest.mock import Mock
from box.findtools.objname import ObjnameConstraint

class ObjnameConstraintTest_match(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(objname='objname')
    
    def test___call__(self):
        constraint = ObjnameConstraint('objname')
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)
          
    def test___call___with_objname_is_regex(self):
        mapper = ObjnameConstraint(re.compile('o.*'))
        mapper(self.emitter)
        self.assertFalse(self.emitter.skip.called)


class ObjnameConstraintTest_not_match(ObjnameConstraintTest_match):

    #Public
    
    def test___call__(self):
        constraint = ObjnameConstraint('x')
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
          
    def test___call___with_objname_is_regex(self):
        constraint = ObjnameConstraint(re.compile('x.*'))
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)