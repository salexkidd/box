import os
import re
import fnmatch
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint


class FilepathConstraint(PatternConstraint):

    # Public

    def __init__(self, basedir=None):
        self._basedir = basedir
        super().__init__()

    def extend(self, name, value):
        if name == 'filepath':
            self._include.append(value)
        if name == 'notfilepath':
            self._exclude.append(value)

    # TODO: don't work with pattern like './pattern'
    def match(self, emitter, pattern):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, emitter.filepath):
                return True
        else:
            if os.path.isabs(pattern):
                pattern = os.path.relpath(pattern, start=self._basedir)
            # TODO: it's not working like glob, bug?
            if fnmatch.fnmatch(emitter.filepath, pattern):
                return True
        return False
