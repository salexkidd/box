import os

class FindFilesMaxdepthMapper:
    
    #Public
    
    def __init__(self, basedir, maxdepth):
        self._basedir = basedir
        self._maxdepth = maxdepth
        
    def __call__(self, emitter):
        if self._maxdepth:
            depth = self._calculate_depth(emitter.filepath)
            if depth > self._maxdepth:
                emitter.skip()
                emitter.stop()
    
    #Protected
    
    def _calculate_depth(self, filepath):
        relpath = os.path.relpath(filepath, start=self._basedir)
        depth = relpath.count(os.path.sep)+1
        return depth