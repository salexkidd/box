import re
import fnmatch
from ...types import RegexCompiledPatternType

class FindFilesFilenameMapper:
    
    #Public
    
    def __init__(self, filename):
        self._filename = filename
        
    def __call__(self, emitter):
        if self._filename:
            if isinstance(self._filename, RegexCompiledPatternType):
                if not re.match(self._filename, emitter.filename):
                    emitter.skip()
            else:
                if not fnmatch.fnmatch(emitter.filename, self._filename):
                    emitter.skip()