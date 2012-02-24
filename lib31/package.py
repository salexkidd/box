import os
import sys
import imp
from setuptools import find_packages
from abc import ABCMeta, abstractproperty
from .reader import Reader
from .decorators.cachedproperty import cachedproperty

class Package(dict):
    
    __metaclass__ = ABCMeta
    
    @abstractproperty
    def NAME(self):
        pass
    
    @abstractproperty
    def URL(self):
        pass
    
    def __init__(self):
        self.update([(name.lower(), getattr(self, name)) 
                     for name in Package.__dict__ #TODO: fix!!!
                     if not name.startswith('_')])    
  
    @property
    def version(self):
        path = self._reader.path(self._main_package)
        meta = imp.find_module('version', [path])
        module = imp.load_module('version', *meta)
        meta[0].close()
        return module.Version()

    @cachedproperty
    def packages(self):
        return find_packages(where=self._reader.path(),
                             exclude=['tests*'])
    
    @cachedproperty
    def long_description(self):
        return self._reader.read('README.rst')
    
    @cachedproperty   
    def download_url(self):
        return ('{url}/tarball/{version}'.
                format(url=self.URL,
                       version=self.version))
    
    @cachedproperty
    def _main_package(self):
        matched = [package for package in self.packges 
                   if '.' not in package]
        if len(matched) == 1:
            return matched[0]
        else:
            raise Exception('Can\'t define main package from {packages}'.
                            format(packages=repr(self.packages)))
    
    @cachedproperty
    def _reader(self):
        module = sys.modules[self.__module__]
        return Reader(os.path.dirname(module.__file__))