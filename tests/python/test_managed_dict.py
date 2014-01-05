import unittest
from unittest.mock import Mock
from lib31.python.managed_dict import ManagedDict

class ManagedDictTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.MockManagedDict = self._make_mock_managed_dict_class()
        self.dict = self.MockManagedDict({'key1': 'value1'})
    
    def test_clear(self):
        self.dict.clear()
        self.dict.__delitem__.assert_called_once_with('key1')
        
    def test_pop(self):
        self.assertEqual(self.dict.pop('key1'), 'value1')
        self.dict.__delitem__.assert_called_once_with('key1')
        
    def test_popitem(self):
        self.assertEqual(self.dict.popitem(), ('key1', 'value1'))
        self.dict.__delitem__.assert_called_once_with('key1')
        
    def test_popitem_with_empty_dict(self):
        self.dict = self.MockManagedDict()
        self.assertRaises(KeyError, self.dict.popitem)      
        
    def test_setdefault(self):
        self.assertEqual(self.dict.setdefault('key2', 'value2'), 'value2')
        self.dict.__setitem__.assert_called_once_with('key2', 'value2')
    
    def test_update_with_dict(self):
        self.dict.update({'key2': 'value2'})
        self.dict.__setitem__.assert_called_once_with('key2', 'value2')
        
    def test_update_with_key_value_pairs(self):
        self.dict.update([('key2', 'value2')])
        self.dict.__setitem__.assert_called_once_with('key2', 'value2')
        
    def test_update_with_kwargs(self):
        self.dict.update(key2='value2')
        self.dict.__setitem__.assert_called_once_with('key2', 'value2')                 
        
    #Protected
    
    def _make_mock_managed_dict_class(self):
        class MockManagedDict(ManagedDict):
            __setitem__ = Mock()
            __delitem__ = Mock()
        return MockManagedDict     