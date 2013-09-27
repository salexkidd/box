class cachedproperty(object):
    """
    Property with caching
    """
    
    #Public
    
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self._fget = fget
        self._fset = fset
        self._fdel = fdel
        self.__doc__ = doc
               
    def __get__(self, obj, cls):
        cache = self._get_object_cache(obj)
        name = self._get_property_name(obj)
        if name not in cache:
            if self._fget:
                cache[name] = self._fget(obj)
            else:
                raise AttributeError('Can\'t get attribute')
        return cache[name]

    def __set__(self, obj, value):
        if self._fset:
            self._fset(obj, value)
        else:
            raise AttributeError('Can\'t set attribute')
    
    def __delete__(self, obj):
        if self._fdel:
            self._fdel(obj)
        else:
            raise AttributeError('Can\'t delete attribute')        
        
    def setter(self, fset):
        self._fset = fset
        return self
    
    def deleter(self, fdel):
        self._fdel = fdel
        return self
    
    @classmethod
    def set(cls, obj, name, value):
        cache = cls._get_object_cache(obj)
        cache[name] = value
        
    @classmethod
    def reset(cls, obj, name):
        cache = cls._get_object_cache(obj)
        cache.pop(name, None)
            
    #Protected
    
    _obj_cache_attribute_name = '_lib31_cached_properties'
    
    @classmethod
    def _get_object_cache(cls, obj):
        return obj.__dict__.setdefault(cls._obj_cache_attribute_name, {})
    
    def _get_property_name(self, obj):
        if not hasattr(self, '_property_name'):
            for scope in obj.__class__.__mro__:       
                for name, value in vars(scope).items():
                    if self is value:
                        self._property_name = name
                        break
                else:
                    continue
                break
            else:
                raise AttributeError('Can\'t determine property name')
        return self._property_name