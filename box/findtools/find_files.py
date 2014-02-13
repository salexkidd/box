import os
import re
import fnmatch
from ..functools import FunctionCall
from ..itertools import map_reduce, MapEmmiter
from ..types import RegexCompiledPatternType

class find_files(FunctionCall):

    #Public
    
    default_basedir = '.'

    def __init__(self, filename=None, basedir=None, max_depth=None, 
                 mappers=[], reducers=[]):
        self._filename = filename
        self._basedir = basedir
        self._max_depth = max_depth
        self._mappers = mappers
        self._reducers = reducers
        if not self._basedir:
            self._basedir = self.default_basedir
            
    def __call__(self):
        files = self._get_files()        
        mappers = self._builtin_mappers+self._mappers
        values = map_reduce(files, mappers, self._reducers)
        return values            
            
    #Protected
            
    _walk_function = staticmethod(os.walk)
    
    def _get_files(self):
        #TODO: os.walk swallow exception if onerror=None
        for dirpath, _, filenames in self._walk_function(self._basedir):       
            for filename in filenames:
                file = os.path.join(dirpath, filename)
                yield MapEmmiter(file, file=file) 
        
    @property        
    def _builtin_mappers(self):
        return [FindFilesMaxDepthMapper(self._basedir, self._max_depth),
                FindFilesFilenameMapper(self._filename)]          


class FindFilesMaxDepthMapper:
    
    #Public
    
    def __init__(self, basedir, max_depth):
        self._basedir = basedir
        self._max_depth = max_depth
        
    def __call__(self, emitter):
        if self._max_depth:
            depth = self._calculate_depth(emitter.file)
            if depth > self._max_depth:
                emitter.skip()
                emitter.stop()
    
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

    
class FindFilesFilenameMapper:
    
    #Public
    
    def __init__(self, filename):
        self._filename = filename
        
    def __call__(self, emitter):
        if self._filename:
            filename = os.path.basename(emitter.file)
            if isinstance(self._filename, RegexCompiledPatternType):
                if not re.match(self._filename, filename):
                    emitter.skip()
            else:
                if not fnmatch.fnmatch(filename, self._filename):
                    emitter.skip()