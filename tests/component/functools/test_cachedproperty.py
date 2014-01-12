import unittest
from unittest.mock import Mock
from box.functools.cachedproperty import cachedproperty

class cachedpropertyTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.CachedpropertyConsumer = self._make_cachedproperty_consumer_class()
        self.consumer = self.CachedpropertyConsumer()
        self.consumer.default_property_value = 'old_value'
        
    def test___get__(self):
        self.assertEqual(self.consumer.property, 'old_value')
        self.consumer.default_property_value = 'new_value'
        self.assertEqual(self.consumer.property, 'old_value')        
    
    def test___get___with_no_property(self):
        self.assertRaises(AttributeError, 
            getattr, self.consumer, 'no_property')
        
    def test___set__(self):
        self.assertEqual(self.consumer.property, 'old_value')        
        self.consumer.property = 'new_value'
        self.assertEqual(self.consumer.property, 'new_value')
        
    def test___set___with_no_property(self):
        self.assertRaises(AttributeError, 
            setattr, self.consumer, 'no_property', 'value')
           
    def test___delete__(self):
        self.assertEqual(self.consumer.property, 'old_value')
        self.consumer.property = 'new_value'                
        del self.consumer.property
        self.assertEqual(self.consumer.property, 'old_value')
        
    def test___delete___with_no_property(self):
        self.assertRaises(
            AttributeError, delattr, 
            self.consumer, 'no_property'
        )
   
    def test___doc___(self):
        prop = cachedproperty()
        self.assertEqual(prop.__doc__, None)
          
    def test___doc___with_doc(self):
        prop = cachedproperty(doc='doc')
        self.assertEqual(prop.__doc__, 'doc')
        
    def test___doc___with_fget(self):
        fget = Mock(__doc__='doc')
        prop = cachedproperty(fget=fget)
        self.assertEqual(prop.__doc__, 'doc')  
        
    #Protected
    
    def _make_cachedproperty_consumer_class(self):           
        class CachedpropertyConsumer:      
            #Public
            def __init__(self):
                self.default_property_value = {}
            property = cachedproperty()
            @property.getter
            def property(self):
                return self.default_property_value
            @property.setter
            def property(self, value):
                cachedproperty.set(self, 'property', value)  
            @property.deleter
            def property(self):
                cachedproperty.reset(self, 'property')
            no_property = cachedproperty()
        return CachedpropertyConsumer