import unittest
from lib31.decorators.cachedproperty import cachedproperty

#Fixtures
class Test(object):
    
    value = 1
    
    @cachedproperty
    def property(self):
        return self.value
    
    @property.setter
    def property(self, value):
        cachedproperty.set(self, 'property', value)
        
    @property.deleter
    def property(self):
        cachedproperty.reset(self, 'property')        
  
    
#Tests
class CachedPropertyTest(unittest.TestCase):
    
    def setUp(self):
        self.test = Test()
        
    def test(self):
        self.assertEqual(self.test.property, 1)
        self.test.value = 2
        self.assertEqual(self.test.property, 1)
        self.test.property = 2
        self.assertEqual(self.test.property, 2)
        del self.test.property
        self.test.value = 3
        self.assertEqual(self.test.property, 3)