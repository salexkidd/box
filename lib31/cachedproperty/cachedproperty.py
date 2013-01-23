class Cachedproperty(object):
    """
    Cachedproperty decorator class.
    """

    #Public

    def __call__(self, func):
        """
        Returns cached property.
        """
        def get(obj, *args, **kwargs):
            name = func.func_name
            cache = self._get_cache(obj)
            try:
                return cache[name] 
            except KeyError:
                cache[name] = func(obj, *args, **kwargs)
                return cache[name]   
        return property(get)
    
    @classmethod
    def set(cls, obj, name, value):
        """
        Sets value to object cached property with name.
        """
        cls._get_cache(obj)[name] = value
    
    @classmethod
    def reset(cls, obj, name=None):
        """
        Resets object cache or
        resets object property cache if name's been passed.
        """
        if not name:
            cls._get_cache(obj).clear()            
        else:
            cls._get_cache(obj).pop(name, None)           
    
    #Protected
                
    @classmethod    
    def _get_cache(cls, obj):
        return obj.__dict__.setdefault(
            cls. _cached_properties_attribute_name, {}
        )

    _cached_properties_attribute_name = '_cached_properties'
    
    
cachedproperty = Cachedproperty()