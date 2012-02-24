import os
import imp
from setuptools import find_packages

class Package(dict):

    def __init__(self):
        self.update([(name.lower(), getattr(self, name)) 
                     for name in Package.__dict__ #TODO: fix!!!
                     if not name.startswith('_')])    
        
    @property
    def version(self):
        path = os.path.join(os.path.dirname(__file__), 'run')
        meta = imp.find_module('version', [path])
        module = imp.load_module('version', *meta)
        meta[0].close()
        return module.Version()
    
    @version.setter
    def version(self, version):
        code = version.code
        with open(self.version.path, 'w') as f:
            f.write(code)
        self['version'] = self.version

    @property
    def packages(self):
        return find_packages(exclude=['tests*'])
    
    @property
    def long_description(self):
        with open('README.rst') as f: #TODO: fix!!!
            return f.read()
    
    @property    
    def download_url(self):
        return ('{url}/tarball/{version}'.
                format(url=self.URL,
                       version=self.version))