class SettingsMetaclass(type):
    
    #Public
    
    def __call__(self, settings=None, **kwargs):
        settings = dict.__new__(self)
        esettings = self.merge_extensions()
        esettings.update(settings)
        settings.__init__(settings=esettings, **kwargs)
        return settings
    
    def merge_extensions(self):
        settings = {}
        for extension in self._extensions:
            if isinstance(extension, dict):
                settings.update(extension)
        return settings
        

class Settings(dict, metaclass=SettingsMetaclass):
    
    #Public
    
    def __init__(self, settings=None, **kwargs):
        self.clear()
        if settings:
            vars(self).update(settings)
        vars(self).update(kwargs)
        self.update(self._as_dict)
        
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        type(self).__init__(self)
        
    def __delattr__(self, name):
        super().__delattr__(name)
        type(self).__init__(self)
                    
    #Protected
    
    _extensions = []    
    
    @property
    def _as_dict(self):
        items = {}
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                if not callable(value):
                    items[name] = value
        return items