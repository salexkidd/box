from ...glob import filtered_iglob
from ...itertools import map_reduce
from ...os import balanced_walk
from ...types import RegexCompiledPatternType
from ..not_found import NotFound
from .emitter import FindFilesEmitter
from .maxdepth import FindFilesMaxdepthMapper
from .filename import FindFilesFilenameMapper
from .filepath import FindFilesFilepathMapper

class find_files(map_reduce):

    #Public
    
    default_basedir = '.'
    default_emitter = FindFilesEmitter

    def __init__(self, filename=None, filepath=None, *,
                 basedir=None, maxdepth=None, 
                 onwalkerror=None, **kwargs):
        self._filename = filename
        self._filepath = filepath
        self._basedir = basedir
        self._maxdepth = maxdepth
        self._onwalkerror = onwalkerror
        if not self._basedir:
            self._basedir = self.default_basedir
        super().__init__(**kwargs)
            
    #Protected
            
    _getfirst_exception = NotFound
    _glob_function = staticmethod(filtered_iglob)
    _walk_function = staticmethod(balanced_walk)
    
    @property
    def _extension_values(self):
        if (self._filepath != None and
            not isinstance(self._filepath, RegexCompiledPatternType)):
            #We have a glob pattern
            glob = self._glob_function
            for filepath in glob(self._filepath, files=True):
                #Emits every file gotten from glob by pattern
                yield self._emitter(filepath, filepath=filepath) 
        else:
            #No glob pattern
            walk = self._walk_function
            for filepath in walk(self._basedir, onerror=self._onwalkerror):
                #Emits every file gotten from walk in basedir
                yield self._emitter(filepath, filepath=filepath) 

    @property        
    def _extension_mappers(self):
        return [FindFilesMaxdepthMapper(self._basedir, self._maxdepth),
                FindFilesFilenameMapper(self._filename),
                FindFilesFilepathMapper(self._filepath)]