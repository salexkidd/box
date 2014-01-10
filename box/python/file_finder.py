import os
import re
import fnmatch
from abc import ABCMeta, abstractmethod

class FileFinder:

    #Public

    def find(self, filename=None, basedir='.', max_depth=0, 
             filters=[], iterators=[], processors=[], reducers=[]):
        if filename:
            filters = [FileFinderFilenameFilter(filename)]+filters
        files = self._find(basedir, max_depth, filters, iterators, processors)
        reduced_files = self._reduce(files, reducers)
        return reduced_files
            
    #Protected
    
    _walk_operator = staticmethod(os.walk)
    
    def _find(self, basedir, max_depth, filters, iterators, processors):
        for dirpath, _, filenames in self._walk_operator(basedir):
            depth = self._calculate_depth(basedir, dirpath)
            if  depth > max_depth:
                break            
            for filename in filenames:
                file = os.path.join(dirpath, filename)
                if not self._filter(file, filters):
                    continue
                if not self._iterate(file, iterators):
                    continue
                processed_file = self._process(file, processors)
                yield processed_file
    
    def _filter(self, file, filters):
        for fltr in filters:
            if not fltr(file):
                return False
        return True
    
    def _iterate(self, file, iterators):
        for iterator in iterators:
            if not iterator(file):
                return False
        return True    
    
    def _process(self, file, processors):
        processed_file = file
        for processor in processors:
            processed_file = processor(processed_file)
        return processed_file
    
    def _reduce(self, files, reducer):
        reduced_files = files
        for reducer in reducer:
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
    
    
class FileFinderFilter(metaclass=ABCMeta):
    
    #Public
           
    @abstractmethod
    def __call__(self, file, *args, **kwargs):
        pass #pragma: no cover
    
    
class FileFinderFilenameFilter(FileFinderFilter):
    
    #Public
    
    def __init__(self, filename):
        self._filename = filename
        
    def __call__(self, file, *args, **kwargs):
        filename = os.path.basename(file)
        if self._is_object_regexp_compiled_pattern(self._filename):
            if not re.match(self._filename, filename):
                return False
        else:
            if not fnmatch.fnmatch(filename, self._filename):
                return False
        return True
    
    def _is_object_regexp_compiled_pattern(self, obj):
        return isinstance(obj, type(re.compile('')))    