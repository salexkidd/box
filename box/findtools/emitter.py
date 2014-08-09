import os
from ..itertools import Emitter


class FindEmitter(Emitter):
    """Emitter representation for find framework.
    """

    # Public

    pass


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
