import os
import re
import sys
import base64
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
        name = '_'.join(self._path.split(os.path.sep)).strip('_')
        name = '_'.join(['virtual_package_from', name])
        name = self._escape_name(name)
        return name

    @cachedproperty
    def __path__(self):
        return [self._path]
    
    #Protected
    
    def _set_path(self, path):
        self._path = os.path.abspath(path)
          
    def _register(self):
        sys.modules[self.__name__] = self
                
    def _escape_name(self, name):
        letters = []
        for letter in name:
            if re.search('[^\w]', letter):
                letter = base64.b16encode(letter.encode()).decode()
            letters.append(letter)
        return ''.join(letters)    