import unittest
from box.itertools.map_reduce import map_reduce

class map_reduce_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.iterable = ['value1', 'value2']
        
    def test(self):
        result = list(map_reduce(self.iterable))
        self.assertEqual(result, ['value1', 'value2'])
        
    def test_with_mapper_using_set_and_get_value(self):
        mapper = lambda emitter: emitter.value(emitter.value()+'!')
        result = list(map_reduce(self.iterable, mappers=[mapper]))
        self.assertEqual(result, ['value1!', 'value2!'])
    
    def test_with_mapper_using_emit_with_condition(self):
        mapper1 = lambda emitter: emitter.emit('emitted1')
        mapper2 = (lambda emitter: 
            emitter.emit('emitted2', emitter.value() == 'value1'))
        result = list(map_reduce(self.iterable, mappers=[mapper1, mapper2]))
        self.assertEqual(result, ['emitted1', 'emitted2', 'emitted1'])
           
    def test_with_mapper_using_skip(self):
        mapper = lambda emitter: emitter.skip()
        result = list(map_reduce(self.iterable, mappers=[mapper]))
        self.assertEqual(result, [])
        
    def test_with_mapper_using_stop(self):
        mapper = lambda emitter: emitter.stop()
        result = list(map_reduce(self.iterable, mappers=[mapper]))
        self.assertEqual(result, ['value1'])
        
    def test_with_mapper_using_stop_and_skip(self):
        #Test ensures that map will stop on step with stop and skip
        mapper1 = lambda emitter: emitter.stop()
        def mapper2(emitter):
            if emitter.value() == 'value1':
                emitter.skip()
        result = list(map_reduce(self.iterable, mappers=[mapper1, mapper2]))
        self.assertEqual(result, [])                        
        
    def test_with_reducer(self):
        reducer = lambda result: 'reduced'
        result = map_reduce(self.iterable, reducers=[reducer])
        self.assertEqual(result, 'reduced')
        
    def test_with_getfirst(self):
        result = map_reduce(self.iterable, getfirst=True)
        self.assertEqual(result, 'value1')
        
    def test_with_getfirst_and_not_values(self):
        self.assertRaises(Exception, map_reduce, [], getfirst=True)
    
    def test_with_fallback_is_none_and_error(self):
        self.assertRaises(Exception, map_reduce, [], getfirst=True)
         
    def test_with_fallback_is_value_and_error(self):
        result = map_reduce([], getfirst=True, fallback='fallback')
        self.assertEqual(result, 'fallback')
        
    def test_with_fallback_is_exception_and_error(self):
        self.assertRaises(RuntimeError, 
            map_reduce, [], getfirst=True, fallback=RuntimeError())
        
    def test_with_fallback_is_callable_and_error(self):
        result = map_reduce([], getfirst=True, fallback=lambda excp: 'excp')
        self.assertEqual(result, 'excp')           