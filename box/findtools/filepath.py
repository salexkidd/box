import os
import re
import fnmatch
from ..glob import filtered_iglob
from ..os import balanced_walk
from ..types import RegexCompiledPatternType
from .condition import Condition

class FilepathCondition(Condition):
    
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
    
    def _effective_match(self, pattern, value):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, value):
                return True
        else:
            if os.path.isabs(pattern):
                pattern = os.path.relpath(pattern, start=self._basedir)
            if fnmatch.fnmatch(value, pattern):
                return True
        return False
    

class FilepathMapper:
    
    #Public
    
    def __init__(self, condition):
        self._condition = condition
    
    def __bool__(self):
        return bool(self._condition)
    
    def __call__(self, emitter):
        if not self._condition.match(emitter.filepath):
            emitter.skip()             