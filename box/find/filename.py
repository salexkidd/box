import re
import fnmatch
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint


class FilenameConstraint(PatternConstraint):

    # Public

    def extend(self, name, value):
        if name == 'filename':
            self._include.append(value)
        if name == 'notfilename':
            self._exclude.append(value)

    def match(self, emitter, pattern):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, emitter.filename):
                return True
        else:
            if fnmatch.fnmatch(emitter.filename, pattern):
                return True
        return False
