import os
from itertools import chain
from ..functools import cachedproperty
from ..importlib import inject
from ..glob import enhanced_iglob
from ..os import balanced_walk, enhanced_join
from .maxdepth import MaxdepthConstraint
from .filename import FilenameConstraint
from .filepath import FilepathConstraint
from .find import find, FindEmitter


class find_files(find):
    """Find files using map_reduce framework.

    :param list filters: find filters
    :param bool join: if True joins resulted filepath with basedir
    :param str basedir: base directory to find
    :param list filepathes: list of filepathes or globs where to find
    :param dict params: map_reduce params

    :returns mixed: map_reduced files
    """

    # Public

    default_emitter = inject('FindFilesEmitter', module=__name__)

    def __init__(self, *, join=False,
                 basedir=None, filepathes=None, **find_params):
        self._join = join
        self._basedir = basedir
        self._filepathes = filepathes
        super().__init__(**find_params)

    # Protected

    _glob = staticmethod(enhanced_iglob)
    _walk = staticmethod(balanced_walk)

    @cachedproperty
    def _values(self):
        for filepath in self._effective_filepathes:
            # Emits every file in filepathes
            file = filepath
            if self._join:
                file = enhanced_join(self._basedir, filepath)
            yield self._emitter(
                file, filepath=filepath, basedir=self._basedir)

    @cachedproperty
    def _effective_constraints(self):
        constraints = [
            MaxdepthConstraint(),
            FilenameConstraint(),
            FilepathConstraint(self._basedir)]
        constraints += super()._effective_constraints
        return constraints

    @cachedproperty
    def _effective_filepathes(self):
        if self._filepathes is not None:
            # We have pathes or globs
            # TODO: fix it's not LAZY load
            chunks = []
            for filepath in self._filepathes:
                chunk = self._glob(
                    filepath,
                    basedir=self._basedir, sorter=sorted, mode='files')
                chunks.append(chunk)
            filepathes = chain(*chunks)
        else:
            # We have to walk fully
            filepathes = self._walk(
                basedir=self._basedir, sorter=sorted, mode='files')
        return filepathes


class FindFilesEmitter(FindEmitter):
    """Emitter representation for find_files.

    Additional attributes:

    - filepath
    - basedir
    """

    # Public

    @property
    def filename(self):
        return os.path.basename(self.filepath)
