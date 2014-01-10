import os
import re
import fnmatch

class FileFinder:

    #Public

    def find(self, filename, basedir='', max_depth=0, 
             filters=[], iterators=[], reducers=[]):
        files = self._find_files(
            basedir, filename, max_depth, filters, iterators)
        reduced_files = self._reduce_files(files, reducers)
        return reduced_files
            
    #Protected
    
    _walk_operator = staticmethod(os.walk)
    
    def _find_files(self, basedir, pattern, max_depth, filters, iterators):
        for dirpath, _, filenames in self._walk_operator(basedir):
            if self._calculate_depth(basedir, dirpath) > max_depth:
                break            
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if not self._filter_by_filename(filename, pattern):
                    continue
                if not self._filter_by_filepath(filepath, filters):
                    continue
                if not self._iterate_by_filepath(filepath, iterators):
                    continue
                yield filepath
    
    def _reduce_files(self, files, reducers):
        reduced_files = files
        for reducer in reducers:
            reduced_files = reducer(reduced_files)
        return reduced_files
    
    def _calculate_depth(self, basedir, dirpath):
        basedir = os.path.normpath(basedir)
        dirpath = os.path.normpath(dirpath)
        if basedir == dirpath:
            depth = 0
        elif os.path.sep not in dirpath:
            depth = 1
        else:
            subpath = dirpath.replace(basedir+os.path.sep, '', 1)
            depth = subpath.count(os.path.sep)+1
        return depth
    
    def _filter_by_filename(self, filename, pattern):
        if self._is_object_regexp_compiled_pattern(pattern):
            if not re.match(pattern, filename):
                return False
        else:
            if not fnmatch.fnmatch(filename, pattern):
                return False
        return True
    
    def _filter_by_filepath(self, filepath, filters):
        for fltr in filters:
            if not fltr(filepath):
                return False
        return True
    
    def _iterate_by_filepath(self, filepath, iterators):
        for iterator in iterators:
            if not iterator(filepath):
                return False
        return True    
    
    def _is_object_regexp_compiled_pattern(self, obj):
        return isinstance(obj, type(re.compile('')))