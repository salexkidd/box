import os
import re
import fnmatch
from ..itertools import map_reduce, MapEmitter
from ..types import RegexCompiledPatternType

class find_files(map_reduce):

    #Public
    
    default_basedir = '.'
    default_emitter = 'deferred:FindFilesMapEmitter'

    def __init__(self, filename=None, filepath=None, *,
                 basedir=None, maxdepth=None, 
                 mappers=[], reducers=[], emitter=None, 
                 fallback=None, onwalkerror=None, followlinks=False):
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
            
    _walk_function = staticmethod(os.walk)
    
    @property
    def _builtin_values(self):
        walk = self._walk_function(
            self._basedir,
            onerror=self._onwalkerror,
            followlinks=self._followlinks)
        for dirpath, _, filenames in walk:       
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                yield self._emitter(filepath, filepath=filepath) 

    @property        
    def _builtin_mappers(self):
        return [FindFilesMaxdepthMapper(self._basedir, self._maxdepth),
                FindFilesFilenameMapper(self._filename),
                FindFilesFilepathMapper(self._filepath)]
        

class FindFilesMapEmitter(MapEmitter):

    #Public

    @property
    def filename(self):
        return os.path.basename(self.filepath)


class FindFilesMaxdepthMapper:
    
    #Public
    
    def __init__(self, basedir, maxdepth):
        self._basedir = basedir
        self._maxdepth = maxdepth
        
    def __call__(self, emitter):
        if self._maxdepth:
            depth = self._calculate_depth(emitter.filepath)
            if depth > self._maxdepth:
                emitter.skip()
                emitter.stop()
    
    #Protected
    
    def _calculate_depth(self, filepath):
        basedir = os.path.normpath(self._basedir)
        dirpath = os.path.normpath(os.path.dirname(filepath))
        if basedir == dirpath:
            depth = 1
        elif os.path.sep not in dirpath:
            depth = 2
        else:
            subpath = dirpath.replace(basedir+os.path.sep, '', 1)
            depth = subpath.count(os.path.sep)+2
        return depth

    
class FindFilesFilenameMapper:
    
    #Public
    
    def __init__(self, filename):
        self._filename = filename
        
    def __call__(self, emitter):
        if self._filename:
            if isinstance(self._filename, RegexCompiledPatternType):
                if not re.match(self._filename, emitter.filename):
                    emitter.skip()
            else:
                if not fnmatch.fnmatch(emitter.filename, self._filename):
                    emitter.skip()
                    
                    
class FindFilesFilepathMapper:
    
    #Public
    
    def __init__(self, filepath):
        self._filepath = filepath
        
    def __call__(self, emitter):
        if self._filepath:
            if isinstance(self._filepath, RegexCompiledPatternType):
                if not re.match(self._filepath, emitter.filepath):
                    emitter.skip()
            else:
                if not fnmatch.fnmatch(emitter.filepath, self._filepath):
                    emitter.skip()
                    
                    
find_files.default_emitter = FindFilesMapEmitter                          