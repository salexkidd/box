import os
import re
import fnmatch
from ..glob import filtered_iglob
from ..os import balanced_walk
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint

class FilepathConstraint(PatternConstraint):
    
    #Public
    
    def __init__(self, include=None, exclude=None, *, basedir=None):
        self._basedir = basedir
        super().__init__(include, exclude)
    
    def walk(self, basedir=None, onerror=None):
        if (self._include == None or
            isinstance(self._include, RegexCompiledPatternType)):
            #We have to walk
            filepathes = self._walk(
                basedir=basedir, sorter=sorted, mode='files', onerror=onerror)
        else:
            #We have a glob pattern
            filepathes = self._glob(self._include, 
                basedir=basedir, sorter=sorted, mode='files')                       
        return filepathes
                
    #Protected
    
    _glob = staticmethod(filtered_iglob)
    _walk = staticmethod(balanced_walk)    
    
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