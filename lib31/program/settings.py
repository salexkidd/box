class Settings(dict):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.clear()
        self.update(self._as_dict)
        
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        type(self).__init__(self)
        
    def __delattr__(self, name):
        super().__delattr__(name)
        type(self).__init__(self)
                    
    #Protected        
    
    @property
    def _as_dict(self):
        items = {}
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                if not callable(value):
                    items[name] = value
        return items