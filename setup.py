#Generated for lib31 0.7.4 from data/setup.tpl

import os
from setuptools import find_packages, setup

package = {

	#Main
	
    'name':'lib31',
	'version': '0.7.4',
	'packages': find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	'include_package_data': True,
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'Respect31',
    'author_email': 'post@respect31.com',
    'maintainer': 'Respect31',
    'maintainer_email': 'post@respect31.com',
    'license': 'MIT License',    
    'url': 'https://github.com/respect31/lib31',
    'download_url': 'https://github.com/respect31/lib31/tarball/0.7.4',    
    'classifiers': (['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules'],),    
    'description': 'Lib31 is library to provide common functionality.',    
    'long_description': '''#Generated for lib31 0.7.4 from data/README.rst

Lib31
=====
Lib31 is library to provide common functionality.

.. image:: https://secure.travis-ci.org/respect31/lib31.png?branch=master 
     :target: https://travis-ci.org/respect31/lib31 
     :alt: build
.. image:: https://coveralls.io/repos/respect31/lib31/badge.png?branch=master 
     :target: https://coveralls.io/r/respect31/lib31  
     :alt: coverage
.. image:: https://badge.fury.io/py/lib31.png
     :target: http://badge.fury.io/py/lib31
     :alt: index     

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install lib31

Authors
-------
- Respect31 <post@respect31.com>
- roll <roll@respect31.com>

Classifiers
-----------
- Development Status :: 3 - Alpha
- Intended Audience :: Developers
- License :: OSI Approved :: MIT License
- Programming Language :: Python :: 3.3
- Topic :: Software Development :: Libraries :: Python Modules

License
-------
MIT License
```````````
Copyright (c) 2014 Respect31 <post@respect31.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

History
-------
0.7.0
`````
- removed xmlrpc
- added python.ObjectLoader

0.6.0
`````
- removed python.import_*''',
    
}

if __name__ == '__main__':
    setup(**package)