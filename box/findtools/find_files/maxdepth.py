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
        basedir = os.path.normpath(self._basedir)
        dirpath = os.path.normpath(os.path.dirname(filepath))
        if basedir == dirpath:
            depth = 1
        elif os.path.sep not in dirpath:
            depth = 2
        else:
            subpath = dirpath.replace(basedir+os.path.sep, '', 1)
            depth = subpath.count(os.path.sep)+2
        return depth