import unittest
from box.itertools.map_reduce import map_reduce

class map_reduce_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.iterable = ['value1', 'value2']
        
    def test(self):
        values = list(map_reduce(self.iterable))
        self.assertEqual(values, ['value1', 'value2'])
        
    def test_with_mapper(self):
        mapper = lambda emitter: emitter.set_value(emitter.get_value()+'!')
        values = list(map_reduce(self.iterable, mappers=[mapper]))
        self.assertEqual(values, ['value1!', 'value2!'])
        
    def test_with_reducer(self):
        reducer = lambda values: 'reduced'
        elements = map_reduce(self.iterable, reducers=[reducer])
        self.assertEqual(elements, 'reduced')