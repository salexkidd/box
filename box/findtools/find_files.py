import os
from ..dependency import inject
from ..itertools import map_reduce, Emitter
from ..os import enhanced_join
from .not_found import NotFound
from .maxdepth import MaxdepthConstraint
from .filename import FilenameConstraint
from .filepath import FilepathConstraint

class find_files(map_reduce):
    """Find files using map_reduce framework.
    
    :param str/glob/re filename: include filenames
    :param str/glob/re notfilename: exclude filenames
    :param str/glob/re filepath: include filepathes
    :param str/glob/re notfilepath: exclude filepathes
    :param str basedir: base directory to find
    :param bool join: if True joins resulted filepath with basedir
    :param int maxdepth: maximal find depth relatively to basedir
    
    :returns mixed: map_reduce result
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """

    #Public
    
    default_emitter = inject('FindFilesEmitter', module=__name__)

    def __init__(self, *, 
                 filename=None, notfilename=None, 
                 filepath=None, notfilepath=None,
                 basedir=None, join=False, maxdepth=None,
                 **kwargs):
        self._filename = FilenameConstraint(filename, notfilename)
        self._filepath = FilepathConstraint(filepath, notfilepath, 
            basedir=basedir)
        self._basedir = basedir
        self._join = join
        self._maxdepth = MaxdepthConstraint(maxdepth)
        super().__init__(**kwargs)
            
    #Protected
    
    _getfirst_exception = NotFound
            
    @property
    def _system_values(self):
        for filepath in self._filepath.inner_filepathes:
            #Emits every file from walk
            file = filepath
            if self._join:
                file = enhanced_join(self._basedir, filepath)
            yield self._emitter(file, filepath=filepath, basedir=self._basedir)  

    @property        
    def _system_mappers(self):
        mappers = []
        if self._maxdepth:
            mappers.append(self._maxdepth)
        if self._filename:
            mappers.append(self._filename)
        if self._filepath:
            mappers.append(self._filepath)    
        return mappers
    

class FindFilesEmitter(Emitter):

    #Public

    @property
    def filename(self):
        return os.path.basename(self.filepath)    