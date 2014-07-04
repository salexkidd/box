import re
import unittest
from unittest.mock import Mock
from box.findtools.filepath import FilepathConstraint

class FilepathConstraintTest_not_skip(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock(filepath='filepath')
    
    def test___call__(self):
        constraint = FilepathConstraint('f*')
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)
          
    def test___call___with_filepath_is_regex(self):
        constraint = FilepathConstraint(re.compile('f.*'))
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)
        

class FilepathConstraintTest_skip(FilepathConstraintTest_not_skip):

    #Public   
    
    def test___call__(self):
        constraint = FilepathConstraint('x*')
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
            
    def test___call___with_filepath_is_regex(self):
        constraint = FilepathConstraint(re.compile('x.*'))
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)        