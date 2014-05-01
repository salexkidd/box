import os
import inspect
from .findtools import find_objects, NotFound

class SettingsMetaclass(type):
    
    #Public
    
    def __call__(self, settings=None, **kwargs):
        settings = dict.__new__(self)
        esettings = self._merge_extensions()
        esettings.update(settings)
        settings.__init__(settings=esettings, **kwargs)
        return settings
    
    #Protected
    
    _extension_file_pattern = (
        'from box import Settings\n\n'
            'class Settings(Settings):\n\n'
            '    #Public\n\n'
            '    pass')
    
    def _merge_extensions(self):
        settings = {}
        for extension in self._extensions:
            if isinstance(extension, str):
                if os.path.isfile(extension):
                    #Extension's settings file already exists 
                    extension_class = self._find_extension_class(extension)
                    extension = extension_class()
                else:
                    #Extension's settings file has to be created
                    self._create_extension_class(extension)
                    extension = {}
            settings.update(extension)
        return settings
    
    def _find_extension_class(self, filepath):
        try:
            extension_class = find_objects(
                objtype=self.__class__,
                filename=os.path.basename(filepath),
                basedir=os.path.dirname(filepath),
                maxdepth=1,                      
                mappers=[lambda emitter: emitter.skip(
                    inspect.getmodule(emitter.object) != emitter.module)],
                getfirst=True)
        except NotFound:
            raise RuntimeError(
                'Extension\'s settings file "filepath" doesn\'t '
                'contain correct user settings class')
        return extension_class
    
    def _create_extension_class(self, filepath):
        try:
            with open(filepath, 'w') as file:
                file.write(self._extension_file_pattern)
        except IOError:
            raise RuntimeError(
                'Extension\'s settings file is failed '
                'to be created at extension path "filepath"')
        

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