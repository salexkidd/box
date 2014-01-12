import unittest
from unittest.mock import Mock, ANY
from box.itertools.map_reduce import map_reduce

class MapReduceTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.iterable = [('element', 'arg1', 'arg2')]
        
    def test___call__(self):
        elements = list(map_reduce(self.iterable))
        self.assertEqual(elements, ['element'])
        
    def test___call___with_filter(self):
        fltr = Mock(return_value=False)
        elements = list(map_reduce(self.iterable, filters=[fltr]))
        self.assertEqual(elements, [])
        fltr.assert_called_with('element', 'arg1', 'arg2')
        
    def test___call___with_processor(self):
        processor = Mock(return_value='processed')
        elements = list(map_reduce(self.iterable, processors=[processor]))
        self.assertEqual(elements, ['processed'])
        processor.assert_called_with('element', 'arg1', 'arg2')
        
    def test___call___with_breaker(self):
        breaker = Mock(return_value=True)
        elements = list(map_reduce(self.iterable, breakers=[breaker]))
        self.assertEqual(elements, [])
        breaker.assert_called_with('element', 'arg1', 'arg2')
    
    def test___call___with_breaker_break_before(self):
        breaker = Mock(return_value=map_reduce.BREAK_BEFORE)
        elements = list(map_reduce(self.iterable, breakers=[breaker]))
        self.assertEqual(elements, [])
           
    def test___call___with_breaker_break_after(self):
        breaker = Mock(return_value=map_reduce.BREAK_AFTER)
        elements = list(map_reduce(self.iterable, breakers=[breaker]))
        self.assertEqual(elements, ['element'])
        
    def test___call___with_reducer(self):
        reducer = Mock(return_value='reduced')
        elements = map_reduce(self.iterable, reducers=[reducer])
        self.assertEqual(elements, 'reduced')
        reducer.assert_called_with(ANY)                     