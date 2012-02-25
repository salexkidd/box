import os
import re
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
    
    def __init__(self):
        for name in set(map(str.upper, dir(self))):
            if not name.startswith('_'):
                value = getattr(self, name)
                if not hasattr(value, '__call__'):
                    self[name.lower()] = value   
    
    def __getattr__(self, name):
        try:
            return getattr(self, name.lower())
        except AttributeError:
            raise
    
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
        where = os.path.abspath(self._reader.path())
        exclude = self._SETTINGS['packages']['exclude']
        return find_packages(where=where,
                             exclude=exclude)
    
    @cachedproperty
    def description(self): #TODO: improve
        filename = self._SETTINGS['files']['readme']
        with open(self._reader.path(filename)) as f:
            for i, line in enumerate(f):
                line = line.strip()
                if i > 1 and line:
                    return line
                  
    @cachedproperty
    def long_description(self):
        filename = self._SETTINGS['files']['readme']
        return self._reader.read(filename)
                    
    @cachedproperty
    def author(self): #TODO: improve
        filename = self._SETTINGS['files']['authors']
        with open(self._reader.path(filename)) as f:
            for i, line in enumerate(f):
                line = line.strip()
                if i > 1 and line:
                    return (re.search(r'-\s+(.*)\s+<', line).
                            group(1))

    @cachedproperty
    def author_email(self): #TODO: improve
        filename = self._SETTINGS['files']['authors']
        with open(self._reader.path(filename)) as f:
            for i, line in enumerate(f):
                line = line.strip()
                if i > 1 and line:
                    return (re.search(r'<(.*)>', line).
                            group(1))
    
    @cachedproperty
    def maintainer(self):
        return self.AUTHOR 

    @cachedproperty
    def maintainer_email(self):
        return self.AUTHOR_EMAIL

    @cachedproperty
    def url(self):
        pattern = 'https://github.com/{author}/{name}'
        return pattern.format(author=self.AUTHOR.lower(), 
                              name=self.NAME.lower())
    
    @cachedproperty   
    def download_url(self):
        pattern = '{url}/tarball/{version}'
        return pattern.format(url=self.URL, 
                              version=self.VERSION)
        
    @cachedproperty
    def license(self):
        filename = self._SETTINGS['files']['license']
        with open(self._reader.path(filename)) as f:
            return f.readline().strip()

    _SETTINGS = {
        'packages': {
            'exclude': ['tests*'],
        },
        'modules': {
            'version': 'version',
        },
        'files': {
            'authors': 'AUTHORS.rst',
            'license': 'LICENSE.rst',
            'readme': 'README.rst',        
        },
    }
    
    @cachedproperty
    def _main_package(self):
        matched = [package for package in self.PACKAGES
                   if '.' not in package]
        if len(matched) == 1:
            return matched[0]
        else:
            raise Exception((
                'Can\'t define main package.\n'
                'Packages: {packages}'
            ).format(
                packages=repr(self.PAKCAGES)
            ))
    
    @cachedproperty
    def _reader(self):
        module = sys.modules[self.__module__]
        return Reader(os.path.dirname(module.__file__))