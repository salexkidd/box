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
        return "<module '{name}' (virtual-package: {path})>".format(
            name=self.__name__, 
            path=self._path,
        )

    @cachedproperty
    def __name__(self):        
        return 'virtual_package_{hash}'.format(
            hash=hashlib.md5(self._path.encode()).hexdigest()
        )

    @cachedproperty
    def __path__(self):
        return [self._path]
    
    #Protected
    
    def _set_path(self, path):
        self._path = os.path.abspath(path)
          
    def _register(self):
        sys.modules[self.__name__] = self