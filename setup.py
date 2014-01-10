#Builded for box None from _templates/setup.tpl

import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': 'box',
	'version':'None',
	'packages': find_packages(
        os.path.dirname(__file__) or '.', 
        exclude=['tests*']
    ),
	'include_package_data': True,
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'roll',
    'author_email': 'roll@respect31.com',
    'maintainer': 'roll',
    'maintainer_email': 'roll@respect31.com',
    'license': 'MIT License',    
    'url': 'https://github.com/respect31/box',
    'download_url':'https://github.com/respect31/box/tarball/None',    
    'classifiers': ['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],    
    'description': 'Box is library to provide common functionality.',    
    'long_description': '''#Builded for box None from _templates/README.rst

Box
=====================
Box is library to provide common functionality.

.. image:: https://secure.travis-ci.org/respect31/box.png?branch=master 
     :target: https://travis-ci.org/respect31/box 
     :alt: build
.. image:: https://coveralls.io/repos/respect31/box/badge.png?branch=master 
     :target: https://coveralls.io/r/respect31/box  
     :alt: coverage
.. image:: https://badge.fury.io/py/box.png
     :target: http://badge.fury.io/py/box
     :alt: index

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install box

Authors
-------
- roll roll@respect31.com

Maintainers
-----------
- roll roll@respect31.com

License
-------
MIT License
`````````````
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
THE SOFTWARE.''',
    
}

if __name__ == '__main__':
    setup(**package)