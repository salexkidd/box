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
    
    default_emitter = FindFilesEmitter

    def __init__(self, filename=None, filepath=None, *,
                 basedir=None, maxdepth=None, 
                 onwalkerror=None, **kwargs):
        self._filename = filename
        self._filepath = filepath
        self._basedir = basedir
        self._maxdepth = maxdepth
        self._onwalkerror = onwalkerror
        super().__init__(**kwargs)
            
    #Protected
            
    _getfirst_exception = NotFound
    _glob = staticmethod(filtered_iglob)
    _walk = staticmethod(balanced_walk)
    
    @property
    def _extension_values(self):
        if (self._filepath != None and
            not isinstance(self._filepath, RegexCompiledPatternType)):
            #We have a glob pattern
            for filepath in self._glob(
                self._filepath, basedir=self._basedir, files=True):
                #Emits every file by glob for pattern in basedir
                yield self._emitter(filepath, filepath=filepath) 
        else:
            #We don't have a glob pattern
            for _, filepathes in self._walk(
                self._basedir, sorter=sorted, onerror=self._onwalkerror):
                for filepath in filepathes:
                    #Emits every file by walk in basedir
                    yield self._emitter(filepath, filepath=filepath) 

    @property        
    def _extension_mappers(self):
        return [FindFilesMaxdepthMapper(self._basedir, self._maxdepth),
                FindFilesFilenameMapper(self._filename),
                FindFilesFilepathMapper(self._filepath)]