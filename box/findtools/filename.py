import re
import fnmatch
from ..types import RegexCompiledPatternType
from .condition import Condition

class FilenameCondition(Condition):
                
    #Protected
    
    def _effective_match(self, pattern, value):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, value):
                return True
        else:
            if fnmatch.fnmatch(value, pattern):
                return True
        return False


class FilenameMapper:
    
    #Public
    
    def __init__(self, condition):
        self._condition = condition
    
    def __bool__(self):
        return bool(self._condition)
    
    def __call__(self, emitter):
        if not self._condition.match(emitter.filename):
            emitter.skip()