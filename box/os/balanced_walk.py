import os
from ..functools import FunctionCall
from .enhanced_join import enhanced_join
from .enhanced_listdir import enhanced_listdir

class balanced_walk(FunctionCall):
    """Recursevly yield (dirpathes, filepathes) tuple 
    level by level from top to bottom of directory tree.

    :param str/list dirpath: top directory path or list of pathes
    :param function(pathes) sorter: function to sort pathes
    :param function(os.error) onerror: function to handle os.errors
    
    :returns generator: (dirpathes, filepathes) generator
    
    Function doesn't support symbolic links. 
    """
    
    #Public
    
    def __init__(self, dirpath=None, *, sorter=None, onerror=None):
        self._dirpath = dirpath
        self._sorter = sorter
        self._onerror = onerror
        
    def __call__(self):
        if not isinstance(self._dirpath, list):
            dirpathes = [self._dirpath]
        else:
            dirpathes = self._dirpath
        inner_filepathes = []
        inner_dirpathes = []
        for dirpath in dirpathes:
            try:
                for name in self._listdir(dirpath):
                    path = self._join(dirpath, name)
                    if self._islink(path):
                        continue
                    elif self._isfile(path):
                        inner_filepathes.append(path)            
                    elif self._isdir(path):
                        inner_dirpathes.append(path)
            except os.error as exception:
                if self._onerror is not None:
                    self._onerror(exception)
                return
        if self._sorter != None:
            inner_filepathes = self._sorter(inner_filepathes)
            inner_dirpathes = self._sorter(inner_dirpathes)
        yield (inner_dirpathes, inner_filepathes)
        if inner_dirpathes:
            yield from type(self)(
                inner_dirpathes, 
                sorter=self._sorter, 
                onerror=self._onerror)
            
    #Protected
    
    _listdir = staticmethod(enhanced_listdir)
    _join = staticmethod(enhanced_join)
    _islink = staticmethod(os.path.islink)
    _isfile = staticmethod(os.path.isfile)
    _isdir = staticmethod(os.path.isdir)