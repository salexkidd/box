import unittest
from box.itertools.map_reduce import Emitter           

class EmitterTest(unittest.TestCase): 
    
    #Public
    
    def setUp(self):
        self.emitter = Emitter('value', var='var')
    
    def test___getattr__(self):
        self.assertEqual(self.emitter.var, 'var')
        
    def test___getattr___not_existent(self):
        self.assertRaises(AttributeError, 
            getattr, self.emitter, 'not_existent') 