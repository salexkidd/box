import unittest
from lib31.python import cachedproperty

#Tests

class CachedpropertyTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.object = CachedpropertyConsumer(property_value=1)
    
    def test_get(self):
        self.assertEqual(self.object.property, 1)
    
    def test_set(self):
        self.object.property = 0
        self.assertEqual(self.object.property, 0)
         
    def test_reset(self):
        self.object.property = 0
        cachedproperty.reset(self.object, 'property')
        self.assertEqual(self.object.property, 1)
        
        
#Objects

class CachedpropertyConsumer(object):
    
    #Public
    
    def __init__(self, property_value):
        self._property_value = property_value
    
    @cachedproperty
    def property(self):
        return self._property_value
    
    @property.setter
    def property(self, value):
        cachedproperty.set(self, 'property', value)  
         
    @property.deleter
    def property(self):
        cachedproperty.reset(self, 'property')              