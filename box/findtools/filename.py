import re
import fnmatch
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint

class FilenameConstraint(PatternConstraint):

    # Protected

    def _match(self, pattern, emitter):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, emitter.filename):
                return True
        else:
            if fnmatch.fnmatch(emitter.filename, pattern):
                return True
        return False
