import unittest
from lib31.python import cachedproperty

#Tests  

class CachedpropertyConsumerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self._consumer = CachedpropertyConsumer()
        self._consumer.default_property_value = 0
        
    def test_property___get__(self):
        self.assertEqual(self._consumer.property, 0)
        self._consumer.default_property_value = 1
        self.assertEqual(self._consumer.property, 0)        
    
    def test_property___set__(self):
        self.assertEqual(self._consumer.property, 0)        
        self._consumer.property = 1
        self.assertEqual(self._consumer.property, 1)
         
    def test_property___delete__(self):
        self.assertEqual(self._consumer.property, 0)
        self._consumer.property = 1                
        del self._consumer.property
        self.assertEqual(self._consumer.property, 0)
    
    def test___get___with_notdefined_property(self):
        self.assertRaises(
            AttributeError, getattr, 
            self._consumer, 'notdefined_property'
        )
        
    def test___set___with_notdefined_property(self):
        self.assertRaises(
            AttributeError, setattr, 
            self._consumer, 'notdefined_property', 1
        )
        
    def test___delete___with_notdefined_property(self):
        self.assertRaises(
            AttributeError, delattr, 
            self._consumer, 'notdefined_property'
        )               
        
#Fixtures    
    
class CachedpropertyConsumer:      
                
    #Public
    
    def __init__(self):
        self.default_property_value = {}
        
    @cachedproperty
    def property(self):
        return self.default_property_value
    
    @property.setter
    def property(self, value):
        cachedproperty.set(self, 'property', value)  
         
    @property.deleter
    def property(self):
        cachedproperty.reset(self, 'property')

    notdefined_property = cachedproperty()