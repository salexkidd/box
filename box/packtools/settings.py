import os
import inspect
from ..findtools import find_objects

class SettingsMetaclass(type):
    """Metaclass adds extensions functionality to Settings.
    """
    
    #Public
    
    def __call__(self, settings=None, **kwargs):
        settings = dict.__new__(self)
        esettings = self._merge_extensions()
        esettings.update(settings)
        settings.__init__(settings=esettings, **kwargs)
        return settings
    

class Settings(dict, metaclass=SettingsMetaclass):
    """Settings representation.
    
    :param dict settings: dict to override settings values
    :param dict kwargs: key=value pairs to override settings values
    
    Following example will show common workflow and extensions: 
    
    >>> from box.packtools import Settings
    >>> class Settings(Settings):
    ...   attr1 = 'value1'
    ...   attr2 = 'value2'
    ...   _extensions = [{'attr2': 'new2'}, 'path_to_user_settings']
    ...
    >>> s = Settings(attr1='new1')
    >>> s
    {'attr1': 'new1', 'attr2': 'new2'}
    
    In the example above program also checks path_to_user_settings:
    
    - if file exists and contain Settings subclass program will use it 
    - if file doesn't exist program will create stub Settings file      
    """
    
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
    """List of extensions.
    
    Members should be following types:
    
    - if element is a dict it just override settings values
    - if element is a string it should be a filepath to another Settings
    """
    
    @classmethod    
    def _merge_extensions(cls):
        settings = {}
        for extension in cls._extensions:
            try:
                if isinstance(extension, str):
                    if os.path.isfile(extension):
                        #Extension's settings file already exists 
                        extension_class = cls._find_extension_class(extension)
                        extension = extension_class()
                    else:
                        #Extension's settings file has to be created
                        cls._create_extension_class(extension)
                        extension = {}
                settings.update(extension)
            except Exception as error:
                cls._handle_extension_error(extension, error)
                continue
        return settings
    
    @classmethod    
    def _find_extension_class(cls, extension):
        return find_objects(
            objtype=cls.__class__,
            filepath=extension,
            mappers=[lambda emitter: emitter.skip(
                inspect.getmodule(emitter.object) != emitter.module)],
            getfirst=True)
    
    @classmethod
    def _create_extension_class(cls, extension):
        os.makedirs(os.path.dirname(extension), exist_ok=True)
        with open(extension, 'w') as file:
            file.write(
            'from box.packtools import Settings\n\n'
            'class Settings(Settings):\n\n'
            '    #Public\n\n'
            '    pass')
    
    @classmethod        
    def _handle_extension_error(cls, extensoin, error):
        pass #pragma: no cover
            
    @property
    def _as_dict(self):
        items = {}
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                if not callable(value):
                    items[name] = value
        return items