import unittest
from lib31.python import cachedproperty

#Tests

class CachedpropertyConsumerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self._object = CachedpropertyConsumer(good_property_value=0)
    
    def test_good_property_get(self):
        self.assertEqual(self._object.good_property, 0)
        self._object.good_property_value = 1
        self.assertEqual(self._object.good_property, 0)        
    
    def test_good_property_set(self):
        self.assertEqual(self._object.good_property, 0)        
        self._object.good_property = 1
        self.assertEqual(self._object.good_property, 1)
         
    def test_good_property_delete(self):
        self.assertEqual(self._object.good_property, 0)
        self._object.good_property = 1                
        del self._object.good_property
        self.assertEqual(self._object.good_property, 0)
        
    def test_bad_property_get(self):
        self.assertRaises(
            AttributeError, getattr, self._object, 'bad_property'
        )
    
    def test_bad_property_set(self):
        self.assertRaises(
            AttributeError, setattr, self._object, 'bad_property', 1
        )
        
    def test_bad_property_delete(self):
        self.assertRaises(
            AttributeError, delattr, self._object, 'bad_property'
        )
        
    def test_non_existent_property_set(self):
        self.assertRaises(
            AttributeError, cachedproperty.set, 
            self._object, 'non_existent_property', 1,
        )         
        
        
#Objects

class CachedpropertyConsumer(object):
    
    #Public
    
    def __init__(self, good_property_value):
        self.good_property_value = good_property_value
    
    @cachedproperty
    def good_property(self):
        return self.good_property_value
    
    @good_property.setter
    def good_property(self, value):
        cachedproperty.set(self, 'good_property', value)  
         
    @good_property.deleter
    def good_property(self):
        cachedproperty.reset(self, 'good_property')
        
    bad_property = cachedproperty()             