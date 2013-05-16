class cachedproperty(object):
    
    #Public
    
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self._fget = fget
        self._fset = fset
        self._fdel = fdel
        self.__doc__ = doc
               
    def __get__(self, object, type):
        if not hasattr(self, '_cache'):
            if self._fget:
                self._cache = self._fget(object)
            else:
                raise AttributeError('can\'t get attribute')
        return self._cache

    def __set__(self, object, value):
        if self._fset:
            self._fset(object, value)
        else:
            raise AttributeError('can\'t set attribute')
    
    def __delete__(self, object):
        if self._fdel:
            self._fdel(object)
        else:
            raise AttributeError('can\'t delete attribute')        
        
    def setter(self, fset):
        self._fset = fset
        return self
    
    def deleter(self, fdel):
        self._fdel = fdel
        return self
    
    @staticmethod
    def set(object, name, value):
        property = object.__class__.__dict__[name]
        property._cache = value
        
    @staticmethod
    def reset(object, name):
        property = object.__class__.__dict__[name]
        if hasattr(property, '_cache'):
            del property._cache