import os

class FindFilesMaxdepthMapper:
    
    #Public
    
    def __init__(self, maxdepth):
        self._maxdepth = maxdepth
        
    def __call__(self, emitter):
        if self._maxdepth:
            depth = emitter.filepath.count(os.path.sep)+1
            if depth > self._maxdepth:
                emitter.skip()
                emitter.stop()