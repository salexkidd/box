import unittest
from lib31.types.dri_dict import DRIDict

class DRIDictTest(unittest.TestCase):
    
    def setUp(self):
        DRIDict.DEFAULT = {'required': True, 'immutable': True}
        DRIDict.REQUIRED = ['required']
        DRIDict.IMMUTABLE = ['immutable']
        self.dict = DRIDict({'init': True})
        
    def test_clear(self):
        self.assertRaises(KeyError, self.dict.clear)

    def test_pop(self):
        res = self.dict.pop('init')
        self.assertTrue(res)
        
    def test_pop_required(self):
        self.assertRaises(KeyError, self.dict.pop, 'required')
    
    def test_popitem(self):
        DRIDict.REQUIRED = []
        res = self.dict.popitem()
        self.assertTrue(res)  
        
    def test_popitem_required(self):
        DRIDict.REQUIRED = list(self.dict.keys())
        self.assertRaises(KeyError, self.dict.popitem)
        
    def test_popitem_empty(self):
        DRIDict.REQUIRED = []
        self.dict.clear()
        self.assertRaises(KeyError, self.dict.popitem)
        
    def test_setdefault(self):
        self.dict.setdefault('some', True)
        
    def test_update(self):
        self.dict.update([('init', False)], required=False)
        self.assertFalse(self.dict['init'])
        self.assertFalse(self.dict['required'])
        
    def test_update_immutable(self):
        self.assertRaises(KeyError, self.dict.update, 
                          {'immutable': False})