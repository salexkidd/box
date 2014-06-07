import unittest
from unittest.mock import Mock
from box.itertools.getfirst import GetfirstMapper, GetfirstReducer

class GetfirstMapperTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.emitter = Mock()

    def test___call___with_getfirst_is_true(self):
        mapper = GetfirstMapper(True)
        mapper(self.emitter)
        self.emitter.stop.assert_called_with(if_not_skipped=True)
        
    def test___call___with_getfirst_is_false(self):
        mapper = GetfirstMapper(False)
        mapper(self.emitter)
        self.assertFalse(self.emitter.stop.call_count)
        

class GetfirstReducerTest(unittest.TestCase):

    #Public

    def test___call___with_getfirst_is_true(self):
        reducer = GetfirstReducer(True)
        self.assertEqual(reducer(iter([1, 2])), 1)
        self.assertRaises(GetfirstReducer.default_exception, reducer, [])
        
    def test___call___with_getfirst_is_true_and_exception(self):
        reducer = GetfirstReducer(True, exception=RuntimeError)
        self.assertRaises(RuntimeError, reducer, [])        
        
    def test___call___with_getfirst_is_false(self):
        reducer = GetfirstReducer(False)
        self.assertEqual(list(reducer(iter([1, 2]))), [1, 2])   