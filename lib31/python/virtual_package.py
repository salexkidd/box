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
        self._set_path(path)
        self._register()

    def __repr__(self):
        return '<VirtualPackage from {path}>'.format(
            path=repr(self.__path__)
        )

    @cachedproperty
    def __name__(self):        
        return 'virtual_package_{hash}'.format(
            hash=hashlib.md5(self.__path__.encode()).hexdigest()
        )

    @cachedproperty
    def __path__(self):
        return self._path
    
    @cachedproperty
    def __file__(self):
        return None    
    
    #Protected
    
    def _set_path(self, path):
        self._path = os.path.abspath(path)
          
    def _register(self):
        sys.modules[self.__name__] = self