import re
import fnmatch
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint

class FilenameConstraint(PatternConstraint):
                
    #Protected
    
    def _match(self, pattern, value):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, value):
                return True
        else:
            if fnmatch.fnmatch(value, pattern):
                return True
        return False


class FilenameMapper:
    
    #Public
    
    def __init__(self, constraint):
        self._constraint = constraint
    
    def __bool__(self):
        return bool(self._constraint)
    
    def __call__(self, emitter):
        if not self._constraint.check(emitter.filename):
            emitter.skip()