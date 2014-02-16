from ..functools import FunctionCall
from ..itertools import map_reduce
from ..types import RegexCompiledPatternType
from .find_files import find_files, FindFilesMapEmitter
  
class find_strings(FunctionCall):

    #Public
    
    default_basedir = '.'
    default_emitter = 'deferred:FindStringsMapEmitter'  
    
    def __init__(self, string=None, *,
                 filename=None, filepath=None,  
                 basedir=None, maxdepth=None, 
                 mappers=[], reducers=[], emitter=None, 
                 fallback=None, onwalkerror=None, followlinks=False):
        self._string = string
        self._filename = filename
        self._filepath = filepath        
        self._basedir = basedir
        self._maxdepth = maxdepth
        self._mappers = mappers
        self._reducers = reducers
        self._emitter = emitter
        self._fallback = fallback        
        self._onwalkerror = onwalkerror
        self._followlinks = followlinks        
        if not self._basedir:
            self._basedir = self.default_basedir
        if not self._emitter:
            self._emitter = self.default_emitter
            
    def __call__(self):
        strings = self._get_strings()
        result = map_reduce(strings, 
            mappers=self._effective_mappers, 
            reducers=self._effective_reducers,
            fallback=self._fallback)
        return result
    
    #Protected
        
    _open_function = staticmethod(open)
    _find_files_function = staticmethod(find_files)
    
    def _get_strings(self):
        for filepath in self._get_files():
            with self._open_function(filepath) as fileobj:
                filetext = fileobj.read()
                if isinstance(self._string, RegexCompiledPatternType):
                    for match in self._string.finditer(filetext):
                        has_groups = bool(match.groups())
                        matched_string = match.group(has_groups)
                        yield self._emitter(matched_string, filepath=filepath)
                elif self._string:
                    matches = filetext.count(self._string)
                    for _ in range(matches):
                        yield self._emitter(self._string, filepath=filepath)
                else:
                    yield self._emitter(filetext, filepath=filepath)
                    
    def _get_files(self):
        files = self._find_files_function(
            filename=self._filename,
            filepath=self._filepath,
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror,
            followlinks = self._followlinks)
        return files
    
    @property        
    def _effective_mappers(self):
        return self._builtin_mappers+self._mappers    
    
    @property        
    def _effective_reducers(self):
        return self._builtin_reducers+self._reducers
    
    @property        
    def _builtin_mappers(self):
        return []

    @property        
    def _builtin_reducers(self):
        return []     
  

class FindStringsMapEmitter(FindFilesMapEmitter): pass
find_strings.default_emitter = FindStringsMapEmitter 