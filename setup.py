import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': 'lib31',
	'version': '0.5.0',
	'packages': find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	'include_package_data': True,
    'install_requires': ['packgram>=0.6'],
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'Respect31',
    'author_email': 'post@respect31.com',
    'maintainer': 'Respect31',
    'maintainer_email': 'post@respect31.com',
    'license': 'MIT License',    
    'url': 'https://github.com/respect31/lib31',
    'download_url': 'https://github.com/respect31/lib31/tarball/0.5.0',    
    'classifiers': ['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules'],    
    'description': 'Lib31 is library to provide common functionality.',    
    'long_description': '''Lib31
=====
Lib31 is library to provide common functionality.

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install lib31

Classifiers
-----------
- Development Status :: 3 - Alpha
- Intended Audience :: Developers
- License :: OSI Approved :: MIT License
- Programming Language :: Python :: 3.3
- Topic :: Software Development :: Libraries :: Python Modules

History
-------
0.6.0
`````
- removed python imports
- added ordered class meta

0.5.0
`````
- ported to Python 3.3 without previous version support
- updated application programing interface''',
        
}

if __name__ == '__main__':
    setup(**package)