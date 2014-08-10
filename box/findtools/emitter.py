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

    def __init__(self, value, *, basedir, filepath, **context):
        self._basedir = basedir
        self._filepath = filepath
        super().__init__(value, **context)

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
    """

    # Public

    pass


class FindObjectsEmitter(FindFilesEmitter):
    """Emitter representation for find_objects.
    """

    # Public

    def __init__(self, value, *,
                 basedir, filepath,
                 module, objname, objself, **context):
        self._module = module
        self._objname = objname
        self._objself = objself
        super().__init__(value, basedir=basedir, filepath=filepath, **context)

    @property
    def module(self):
        return self._module

    @property
    def objname(self):
        return self._objname

    @property
    def objself(self):
        return self._objself

    @property
    def objtype(self):
        return type(self.objself)
