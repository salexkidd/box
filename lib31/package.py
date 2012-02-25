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
        pass #pragma: no cover
    
    @abstractproperty
    def URL(self):
        pass #pragma: no cover
    
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                if not hasattr(value, '__call__'):
                    self[name] = value   
    
    def reload(self):
        cachedproperty.reset(self)
        self.__init__()
    
    @cachedproperty
    def version(self):
        name = self._SETTINGS['modules']['version']
        path = self._reader.path(self._main_package)
        meta = imp.find_module(name, [path])
        module = imp.load_module(name, *meta)
        meta[0].close()
        return module.Version()

    @cachedproperty
    def packages(self):
        exclude = self._SETTINGS['exclude']
        return find_packages(where=self._reader.path(),
                             exclude=exclude)
    
    @cachedproperty
    def long_description(self):
        filename = self._SETTINGS['files']['readme']
        return self._reader.read(filename)
    
    @cachedproperty   
    def download_url(self):
        return ('{url}/tarball/{version}'.
                format(url=self.URL,
                       version=self.version))
        
    @cachedproperty
    def license(self):
        filename = self._SETTINGS['files']['license']
        with open(self._reader.path(filename)) as f:
            return f.readline().strip()

    _SETTINGS = {
        'exclude': [
            'tests*'
        ],
        'modules': {
            'version': 'version',
        },
        'files': {
            'authors': 'AUTHORS.rst',
            'license': 'LICENSE.rst',
            'readme': 'README.rst',        
        },
        'patterns': {
            'url': ('https://github.com/'
                    '{author_lowered}/{name_lowered}'),
            'download_url': '{url}/tarball/{version}',             
        }
    }
    
    @cachedproperty
    def _main_package(self):
        matched = [package for package in self.packages 
                   if '.' not in package]
        if len(matched) == 1:
            return matched[0]
        else:
            raise Exception((
                'Can\'t define main package.\n'
                'Packages: {packages}'
            ).format(
                packages=repr(self.packages)
            ))
    
    @cachedproperty
    def _reader(self):
        module = sys.modules[self.__module__]
        return Reader(os.path.dirname(module.__file__))