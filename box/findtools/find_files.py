import os
import re
import fnmatch
from ..itertools import map_reduce
from ..types import RegexCompiledPatternType

class FindFiles:

    #Public
    
    BREAK_BEFORE = map_reduce.BREAK_BEFORE
    BREAK_AFTER = map_reduce.BREAK_AFTER
    
    default_basedir = '.'

    def __call__(self, name=None, basedir=None, max_depth=None, 
             breakers=[], filters=[], processors=[], reducers=[]):
        if not basedir:
            basedir = self.default_basedir        
        breakers = [self._max_depth_breaker_class(basedir, max_depth)]+breakers
        filters = [self._name_filter_class(name)]+filters
        files = self._get_files(basedir)
        map_reduced_files = map_reduce(
            files, breakers, filters, processors, reducers)
        return map_reduced_files
            
    #Protected
    
    _max_depth_breaker_class = property(lambda self: FindFilesMaxDepthBreaker)
    _name_filter_class = property(lambda self: FindFilesNameFilter)
    _walk_operator = staticmethod(os.walk)
    
    def _get_files(self, basedir):
        #TODO: os.walk swallow exception if onerror=None
        for dirpath, _, filenames in self._walk_operator(basedir):       
            for filename in filenames:
                file = os.path.join(dirpath, filename)
                yield (file,) 


class FindFilesCall:

    #Public

    pass


class FindFilesMaxDepthBreaker:
    
    #Public
    
    def __init__(self, basedir, max_depth):
        self._basedir = basedir
        self._max_depth = max_depth
        
    def __call__(self, file):
        if self._max_depth:
            depth = self._calculate_depth(file)
            if depth > self._max_depth:
                return True 
        return False
    
    #Protected
    
    def _calculate_depth(self, file):
        basedir = os.path.normpath(self._basedir)
        filedir = os.path.normpath(os.path.dirname(file))
        if basedir == filedir:
            depth = 1
        elif os.path.sep not in filedir:
            depth = 2
        else:
            subpath = filedir.replace(basedir+os.path.sep, '', 1)
            depth = subpath.count(os.path.sep)+2
        return depth

    
class FindFilesNameFilter:
    
    #Public
    
    def __init__(self, name):
        self._name = name
        
    def __call__(self, file):
        if self._name:
            name = os.path.basename(file)
            if isinstance(self._name, RegexCompiledPatternType):
                if not re.match(self._name, name):
                    return False
            else:
                if not fnmatch.fnmatch(name, self._name):
                    return False
        return True
    
    
find_files = FindFiles()