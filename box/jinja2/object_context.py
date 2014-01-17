class ObjectContext:
    
    #Public
    
    def __init__(self, module):
        self._module = module
        
    def __contains__(self, key):
        return hasattr(self._module, key) 
        
    def __getitem__(self, key):
        try:
            return getattr(self._module, key)
        except AttributeError:
            raise KeyError(key)