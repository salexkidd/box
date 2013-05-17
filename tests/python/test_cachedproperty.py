import unittest
from lib31.python import cachedproperty

#Tests

class CachedpropertyTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self._property = cachedproperty()
    
    def test_get_property_name(self):
        self.assertRaises(
            AttributeError, self._property._get_property_name, None
        )
    

class CachedpropertyConsumerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self._object = CachedpropertyConsumer(property_value=0)
    
    def test_property_get(self):
        self.assertEqual(self._object.property, 0)
        self._object.property_value = 1
        self.assertEqual(self._object.property, 0)        
    
    def test_property_set(self):
        self.assertEqual(self._object.property, 0)        
        self._object.property = 1
        self.assertEqual(self._object.property, 1)
         
    def test_property_delete(self):
        self.assertEqual(self._object.property, 0)
        self._object.property = 1                
        del self._object.property
        self.assertEqual(self._object.property, 0)
        
    def test_not_defined_property_get(self):
        self.assertRaises(
            AttributeError, getattr, 
            self._object, 'not_defined_property'
        )
    
    def test_not_defined_property_set(self):
        self.assertRaises(
            AttributeError, setattr, 
            self._object, 'not_defined_property', 1
        )
        
    def test_not_defined_property_delete(self):
        self.assertRaises(
            AttributeError, delattr, 
            self._object, 'not_defined_property'
        )       
        
        
#Objects

class CachedpropertyConsumer(object):
    
    #Public
    
    def __init__(self, property_value):
        self.property_value = property_value
    
    @cachedproperty
    def property(self):
        return self.property_value
    
    @property.setter
    def property(self, value):
        cachedproperty.set(self, 'property', value)  
         
    @property.deleter
    def property(self):
        cachedproperty.reset(self, 'property')
        
    not_defined_property = cachedproperty()             