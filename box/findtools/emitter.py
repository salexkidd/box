import os
from ..itertools import Emitter


class FindEmitter(Emitter):
    """Emitter representation for find framework.
    """

    # Public

    pass


class FindFilesEmitter(FindEmitter):
    """Emitter representation for find_files.
    """

    # Public

    def __init__(self, file, *, basedir, filepath, **context):
        self._basedir = basedir
        self._filepath = filepath
        super().__init__(file, **context)

    @property
    def basedir(self):
        return self._basedir

    @property
    def filename(self):
        return os.path.basename(self.filepath)

    @property
    def filepath(self):
        return self._filepath


class FindStringsEmitter(FindFilesEmitter):
    """Emitter representation for find_strings.

    Additional attributes:

    - filepath
    - basedir
    """

    # Public

    pass


class FindObjectsEmitter(FindFilesEmitter):
    """Emitter representation for find_objects.

    Additional attributes:

    - object
    - objname
    - module
    - filepath
    - basedir
    """

    # Public

    @property
    def objtype(self):
        return type(self.object)
