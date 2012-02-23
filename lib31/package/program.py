import os
import imp
from setuptools import find_packages

class ProgramPackage(dict):
    
    #Maindata
    NAME = 'run-core'
    ENTRY_POINTS = {
        'console_scripts': [
            'run = run.scripts.run:run',
        ]
    }
    TEST_SUITE = 'nose.collector'
    TESTS_REQUIRE = ['nose']
    
    #Metadata
    DESCRIPTION = (
        'Run is simple but extendable command line '
        'tool to run functions and methods from file.'
    )
    AUTHOR = 'Respect31'
    AUTHOR_EMAIL='team@respect31.com'
    MAINTAINER='Respect31'
    MAINTAINER_EMAIL='team@respect31.com'
    URL='https://github.com/respect31/run-core'
    PLATFORMS=['Unix', 'POSIX']
    LICENSE='MIT license'     
    CLASSIFIERS=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',               
    ]

    def __init__(self):
        self.update([(name.lower(), getattr(self, name)) 
                     for name in ProgramPackage.__dict__ #TODO: fix!!!
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
        with open('README.rst') as f:
            return f.read()
    
    @property    
    def download_url(self):
        return ('{url}/tarball/{version}'.
                format(url=self.URL,
                       version=self.version))