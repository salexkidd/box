import os
from ..dependency import inject
from ..functools import cachedproperty
from ..itertools import map_reduce, Emitter
from ..glob import filtered_iglob
from ..os import balanced_walk, enhanced_join
from ..types import RegexCompiledPatternType
from .not_found import NotFound
from .maxdepth import MaxdepthConstraint
from .filename import FilenameConstraint
from .filepath import FilepathConstraint

class find_files(map_reduce):
    """Find files using map_reduce framework.

    :param str/glob/re filename: include filenames pattern
    :param str/glob/re notfilename: exclude filenames pattern
    :param str/glob/re filepath: include filepathes pattern
    :param str/glob/re notfilepath: exclude filepathes pattern
    :param str basedir: base directory to find
    :param bool join: if True joins resulted filepath with basedir
    :param int maxdepth: maximal find depth relatively to basedir

    :returns mixed: map_reduce result

    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """

    # Public

    default_emitter = inject('FindFilesEmitter', module=__name__)

    def __init__(self, *,
                 filename=None, notfilename=None,
                 filepath=None, notfilepath=None,
                 basedir=None, join=False, maxdepth=None,
                 **kwargs):
        self._filename = filename
        self._notfilename = notfilename
        self._filepath = filepath
        self._notfilepath = notfilepath
        self._basedir = basedir
        self._join = join
        self._maxdepth = maxdepth
        super().__init__(**kwargs)

    # Protected

    _getfirst_exception = NotFound
    _glob = staticmethod(filtered_iglob)
    _walk = staticmethod(balanced_walk)

    @cachedproperty
    def _system_values(self):
        for filepath in self._filepathes:
            # Emits every file in filepathes
            file = filepath
            if self._join:
                file = enhanced_join(self._basedir, filepath)
            yield self._emitter(file, filepath=filepath, basedir=self._basedir)

    @cachedproperty
    def _system_mappers(self):
        mappers = []
        maxdepth = MaxdepthConstraint(self._maxdepth)
        if maxdepth:
            mappers.append(maxdepth)
        filename = FilenameConstraint(self._filename, self._notfilename)
        if filename:
            mappers.append(filename)
        filepath = FilepathConstraint(self._filepath, self._notfilepath,
            basedir=self._basedir)
        if filepath:
            mappers.append(filepath)
        return mappers

    @cachedproperty
    def _filepathes(self):
        if (self._filepath == None or
            isinstance(self._filepath, RegexCompiledPatternType)):
            # We have to walk
            filepathes = self._walk(
                basedir=self._basedir, sorter=sorted, mode='files')
        else:
            # We have a glob pattern
            filepathes = self._glob(self._filepath,
                basedir=self._basedir, sorter=sorted, mode='files')
        return filepathes


class FindFilesEmitter(Emitter):
    """Emitter representation for find_files.

    Additional attributes:

    - filepath
    - basedir
    """

    # Public

    @property
    def filename(self):
        return os.path.basename(self.filepath)
