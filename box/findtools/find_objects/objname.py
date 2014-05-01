from ...types import RegexCompiledPatternType

class FindObjectsObjnameMapper:
    
    #Public
    
    def __init__(self, objname):
        self._objname = objname
        
    def __call__(self, emitter):
        if self._objname:
            if isinstance(self._objname, RegexCompiledPatternType):
                if not self._objname.match(emitter.objname):
                    emitter.skip()
            else:
                if emitter.objname != self._objname:
                    emitter.skip()