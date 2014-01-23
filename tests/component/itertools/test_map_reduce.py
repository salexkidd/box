import unittest
from box.itertools.map_reduce import map_reduce, MapEmmiter

class map_reduce_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.iterable = ['value1', 'value2']
        
    def test(self):
        values = list(map_reduce(self.iterable))
        self.assertEqual(values, ['value1', 'value2'])
        
    def test_with_mapper_using_set_and_get_value(self):
        mapper = lambda emitter: emitter.value(emitter.value()+'!')
        values = list(map_reduce(self.iterable, mappers=[mapper]))
        self.assertEqual(values, ['value1!', 'value2!'])
    
    def test_with_mapper_using_emit_with_condition(self):
        mapper1 = lambda emitter: emitter.emit('emitted1')
        mapper2 = (lambda emitter: 
            emitter.emit('emitted2', emitter.value() == 'value1'))
        values = list(map_reduce(self.iterable, mappers=[mapper1, mapper2]))
        self.assertEqual(values, ['emitted1', 'emitted2', 'emitted1'])
           
    def test_with_mapper_using_skip(self):
        mapper = lambda emitter: emitter.skip()
        values = list(map_reduce(self.iterable, mappers=[mapper]))
        self.assertEqual(values, [])
        
    def test_with_mapper_using_stop(self):
        mapper = lambda emitter: emitter.stop()
        values = list(map_reduce(self.iterable, mappers=[mapper]))
        self.assertEqual(values, ['value1'])                 
        
    def test_with_reducer(self):
        reducer = lambda values: 'reduced'
        elements = map_reduce(self.iterable, reducers=[reducer])
        self.assertEqual(elements, 'reduced')
        
        
class MapEmmiterTest(unittest.TestCase): 
    
    #Public
    
    def setUp(self):
        self.emitter = MapEmmiter('value', var='var')
    
    def test___getattr__(self):
        self.assertEqual(self.emitter.var, 'var')
        
    def test___getattr___not_existent(self):
        self.assertRaises(AttributeError, 
            getattr, self.emitter, 'not_existent')                 