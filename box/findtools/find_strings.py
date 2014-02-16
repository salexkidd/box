from ..itertools import map_reduce
from ..types import RegexCompiledPatternType
from .find_files import find_files, FindFilesMapEmitter
  
class find_strings(map_reduce):

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
        self._onwalkerror = onwalkerror
        self._followlinks = followlinks        
        if not self._basedir:
            self._basedir = self.default_basedir
        super().__init__(
            mappers=mappers, 
            reducers=reducers,
            emitter=emitter, 
            fallback=fallback) 
    
    #Protected
        
    _open_function = staticmethod(open)
    _find_files_function = staticmethod(find_files)
    
    @property
    def _builtin_values(self):
        for filepath in self._files:
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
                    
    @property
    def _files(self):
        files = self._find_files_function(
            filename=self._filename,
            filepath=self._filepath,
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror,
            followlinks = self._followlinks)
        return files 
  

class FindStringsMapEmitter(FindFilesMapEmitter): pass
find_strings.default_emitter = FindStringsMapEmitter 