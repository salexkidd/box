import re
import fnmatch
from ..types import RegexCompiledPatternType

class FilenameMapper:
    
    #Public
    
    def __init__(self, filename):
        self._filename = filename
        
    def __call__(self, emitter):
        if self._filename:
            if not isinstance(self._filename, RegexCompiledPatternType):
                if not fnmatch.fnmatch(emitter.filename, self._filename):
                    emitter.skip()
            else:
                if not re.match(self._filename, emitter.filename):
                    emitter.skip()