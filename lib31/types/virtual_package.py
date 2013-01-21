import os
import sys
import hashlib

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
            path = repr(self.__path__)
        )

    @property
    def __name__(self):        
        return '_'.join([
            'virtual_package',
            hashlib.md5(', '.join(self.__path__)).hexdigest()
        ])

    @property
    def __path__(self):
        return map(os.path.abspath, self._path)
    
    #Protected
            
    def _register(self):
        sys.modules[self.__name__] = self