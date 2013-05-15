import unittest
from box.package.library.cachedproperty import cachedproperty

#Fixtures

class PropertyClassFixture(object):
    
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
  
    
#Tests

class CachedPropertyTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.object = PropertyClassFixture(property_value=1)
    
    def test_get(self):
        self.assertEqual(self.object.property, 1)
    
    def test_set(self):
        self.object.property = 0
        self.assertEqual(self.object.property, 0)
    
    def test_reset_all(self):
        self.object.property = 0
        cachedproperty.reset(self.object)
        self.assertEqual(self.object.property, 1)
        
    def test_reset_concrete(self):
        self.object.property = 0
        cachedproperty.reset(self.object, 'property')
        self.assertEqual(self.object.property, 1)             