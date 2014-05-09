import re
from ..types import RegexCompiledPatternType

class FilepathMapper:
    
    #Public
    
    def __init__(self, filepath):
        self._filepath = filepath
        
    def __call__(self, emitter):
        if self._filepath:
            if isinstance(self._filepath, RegexCompiledPatternType):
                if not re.match(self._filepath, emitter.filepath):
                    emitter.skip()           