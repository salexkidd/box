import os
import re
import fnmatch
from .map_reduce import MapReduce
from .regex_types import RegexCompiledPatternType

class FileFinder:

    #Public

    #TODO: add ignore_errors flag
    def find(self, name=None, basedir='.', max_depth=0, 
             breakers=[], filters=[], processors=[], reducers=[]):
        breakers = [self._max_depth_breaker_class(basedir, max_depth)]+breakers
        filters = [self._name_filter_class(name)]+filters
        files = self._get_files(basedir)
        map_reduce = MapReduce(breakers, filters, processors, reducers)
        map_reduced_files = map_reduce(files)
        return map_reduced_files
            
    #Protected
    
    _max_depth_breaker_class = property(lambda self: FileFinderMaxDepthBreaker)
    _name_filter_class = property(lambda self: FileFinderNameFilter)
    _walk_operator = staticmethod(os.walk)
    
    def _get_files(self, basedir):
        for dirpath, _, filenames in self._walk_operator(basedir):       
            for filename in filenames:
                file = os.path.join(dirpath, filename)
                yield (file,) 
      
      
class FileFinderMaxDepthBreaker:
    
    #Public
    
    def __init__(self, basedir, max_depth):
        self._basedir = basedir
        self._max_depth = max_depth
        
    def __call__(self, file):
        depth = self._calculate_depth(file)
        if depth > self._max_depth:
            return True 
        return False
    
    #Protected
    
    def _calculate_depth(self, file):
        basedir = os.path.normpath(self._basedir)
        filedir = os.path.normpath(os.path.dirname(file))
        if basedir == filedir:
            depth = 0
        elif os.path.sep not in filedir:
            depth = 1
        else:
            subpath = filedir.replace(basedir+os.path.sep, '', 1)
            depth = subpath.count(os.path.sep)+1
        return depth

    
class FileFinderNameFilter:
    
    #Public
    
    def __init__(self, name):
        self._name = name
        
    def __call__(self, file):
        if self._name:
            filtered_name = os.path.basename(file)
            if isinstance(self._name, RegexCompiledPatternType):
                if not re.match(self._name, filtered_name):
                    return False
            else:
                if not fnmatch.fnmatch(filtered_name, self._name):
                    return False
        return True