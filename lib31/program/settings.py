import os
import re
import imp

class Settings(dict):
    
    #Public
    
    def __new__(cls, path=None):
        cls._set_path(path)
        cls = cls._get_class()
        return dict.__new__(cls) 
    
    def __init__(self, *args, **kwargs):
        self.refresh()
    
    def refresh(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                if not callable(value):
                    self[name] = value
    
    #Protected
    
    _pattern = (
        'from {module} import {cls}\n\n'
        'class Settings({cls}):\n'
        '    pass'
    )
    
    @classmethod
    def _set_path(cls, path):
        if path:
            cls._path=path
    
    @classmethod
    def _get_class(cls):
        if getattr(cls, '_path', None):
            try:
                cls._ensure_subclass()
                cls = cls._load_subclass()
            #TODO: add warning
            except Exception:
                del cls._path
        return cls
            
    @classmethod
    def _ensure_subclass(cls):
        if not os.path.exists(cls._path):
            os.makedirs(os.path.dirname(cls._path), exist_ok=True)
            with open(cls._path, 'w') as file:
                file.write(cls._pattern.format(
                    module=cls.__module__,
                    cls=cls.__name__,
                ))
                   
    @classmethod
    def _load_subclass(cls):
        name = re.sub(r'\.py.?$', '', os.path.basename(cls._path))
        path = os.path.dirname(cls._path)
        meta = imp.find_module(name, [path])
        module = imp.load_module(name, *meta)
        meta[0].close()
        return module.Settings