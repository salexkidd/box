import unittest
from unittest.mock import Mock, ANY
from box.python.map_reduce import MapReduce

class MapReduceTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.iterable = [('element', 'arg1', 'arg2')]
        
    def test(self):
        map_reduce = MapReduce()
        self.assertEqual(list(map_reduce(self.iterable)), ['element'])
        
    def test_with_filter(self):
        fltr = Mock(return_value=False)
        map_reduce = MapReduce(filters=[fltr])
        self.assertEqual(list(map_reduce(self.iterable)), [])
        fltr.assert_called_with('element', 'arg1', 'arg2')
        
    def test_with_processor(self):
        processor = Mock(return_value='processed')
        map_reduce = MapReduce(processors=[processor])
        self.assertEqual(list(map_reduce(self.iterable)), ['processed'])
        processor.assert_called_with('element', 'arg1', 'arg2')
        
    def test_with_breaker(self):
        breaker = Mock(return_value=True)
        map_reduce = MapReduce(breakers=[breaker])
        self.assertEqual(list(map_reduce(self.iterable*2)), ['element'])
        breaker.assert_called_with('element', 'arg1', 'arg2')
        
    def test_with_reducer(self):
        reducer = Mock(return_value='reduced')
        map_reduce = MapReduce(reducers=[reducer])
        self.assertEqual(map_reduce(self.iterable), 'reduced')
        reducer.assert_called_with(ANY)                     