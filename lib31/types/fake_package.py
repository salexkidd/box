import os
import sys
import hashlib

class FakePackage(object):
    
    def __init__(self, path):
        self._path = path
        self._register()

    def __repr__(self):
        return '<FakePackage from {path}>'.format(
            path = repr(self.__path__)
        )

    @property
    def __name__(self):        
        return hashlib.md5(', '.join(self.__path__)).hexdigest()

    @property
    def __path__(self):
        return map(os.path.abspath, self._path)
            
    def _register(self):
        sys.modules[self.__name__] = self