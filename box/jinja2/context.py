class ObjectContext:
    
    #Public
    
    def __init__(self, obj):
        self._object = obj
        
    def __contains__(self, key):
        return hasattr(self._object, key) 
        
    def __getitem__(self, key):
        try:
            return getattr(self._object, key)
        except AttributeError:
            raise KeyError(key)