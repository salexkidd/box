import os
import re
import fnmatch
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint

class FilepathConstraint(PatternConstraint):
    
    #Public
    
    def __init__(self, include=None, exclude=None, *, basedir=None):
        self._basedir = basedir
        super().__init__(include, exclude)
                
    #Protected
    
    def _match(self, pattern, emitter):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, emitter.filepath):
                return True
        else:
            if os.path.isabs(pattern):
                pattern = os.path.relpath(pattern, start=self._basedir)
            if fnmatch.fnmatch(emitter.filepath, pattern):
                return True
        return False            