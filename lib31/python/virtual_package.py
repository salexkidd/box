import os
import sys
import hashlib
from .cachedproperty import cachedproperty

class VirtualPackage(object):
    """
    Virtual package with path list.
    """
    
    #Public
    
    def __init__(self, path):
        if path and not isinstance(path, list):
            raise TypeError('Path must be a list like sys.path')         
        self._path = path
        self._register()

    def __repr__(self):
        return '<VirtualPackage from {path}>'.format(
            path=repr(self.__path__)
        )

    @cachedproperty
    def __name__(self):        
        return 'virtual_package_{hash}'.format(
            hash=hashlib.md5(', '.join(self.__path__).encode()).hexdigest()
        )

    @cachedproperty
    def __path__(self):
        return map(os.path.abspath, self._path)
    
    @cachedproperty
    def __file__(self):
        return os.path.join(self._path[0], '__init__.py')    
    
    #Protected
            
    def _register(self):
        sys.modules[self.__name__] = self