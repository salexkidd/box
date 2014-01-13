class ManagedDict(dict):
    """All mutations through __setitem__ and __delitem__"""
    
    #Public
    
    def clear(self):
        for key in self.keys():
            del self[key]
    
    def pop(self, key, default=None):
        value = self.get(key, default)
        del self[key]
        return value
    
    def popitem(self):
        if self:
            (key, value) = list(self.items())[-1]
            del self[key]
            return (key, value)
        else:
            return super().popitem()
    
    def setdefault(self, key, default=None):
        value = self.get(key, default)
        if key not in self:
            self[key] = value
        return value
    
    def update(self, other=None, **kwargs):
        if other != None:
            if hasattr(other, 'keys'):
                for key in other:
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value
        else:
            for key in kwargs:
                self[key] = kwargs[key]