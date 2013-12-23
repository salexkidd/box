class ManagedDict(dict):
    "All mutations through __setitem__ and __delitem__"
    
    #Public
    
    def clear(self):
        for key in list(self.keys()):
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
            return super(ManagedDict, self).popitem()
    
    def setdefault(self, key, default=None):
        value = self.get(key, default)
        self[key] = value
        return value
    
    def update(self, other, **kwargs):
        if hasattr(other, 'keys'):
            for key in other:
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value
        for key in kwargs:
            self[key] = kwargs[key]