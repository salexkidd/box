from ...glob import filtered_iglob
from ...itertools import map_reduce
from ...os import balanced_walk, enhanced_join
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
                 basedir=None, join=False, maxdepth=None, 
                 onwalkerror=None, **kwargs):
        self._filename = filename
        self._filepath = filepath
        self._basedir = basedir
        self._join = join
        self._maxdepth = maxdepth
        self._onwalkerror = onwalkerror
        super().__init__(**kwargs)
            
    #Protected
            
    _getfirst_exception = NotFound
    _glob = staticmethod(filtered_iglob)
    _walk = staticmethod(balanced_walk)
    
    @property
    def _extension_values(self):
        for filepath in self._filepathes:
            file = filepath
            if self._join:
                file = enhanced_join(self._basedir, filepath)
            #Emits every file gotten from filepathes
            yield self._emitter(file, basedir=self._basedir, filepath=filepath)  

    @property        
    def _extension_mappers(self):
        return [FindFilesMaxdepthMapper(self._maxdepth),
                FindFilesFilenameMapper(self._filename),
                FindFilesFilepathMapper(self._filepath)]
    
    @property
    def _filepathes(self):
        if (self._filepath == None or
            isinstance(self._filepath, RegexCompiledPatternType)):
            #We have to walk
            filepathes = self._walk(
                basedir=self._basedir, sorter=sorted, mode='files',
                onerror=self._onwalkerror)            
        else:
            #We have a glob pattern
            filepathes = self._glob(self._filepath, 
                basedir=self._basedir, sorter=sorted, mode='files')
        return filepathes