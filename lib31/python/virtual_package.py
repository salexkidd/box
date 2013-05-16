import os
import sys
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
        return "<module '{name}' (virtual-package)>".format(
            name=self.__name__, 
        )

    @cachedproperty
    def __name__(self):
        return self._path.replace('.', '_')          

    @cachedproperty
    def __path__(self):
        return [self._path]
    
    #Protected
    
    def _set_path(self, path):
        self._path = os.path.abspath(path)
          
    def _register(self):
        sys.modules[self.__name__] = self
        
                
            
        