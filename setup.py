#DO NOT CHANGE THIS FILE. SOURCE IS IN "_sources" DIRECTORY.

import os
from setuptools import find_packages

package = {

	#Main

    'name': 'box',
	'version':'0.31.0',
	'packages': find_packages(
        os.path.dirname(__file__) or '.', 
        exclude=['tests*']
    ),
	'include_package_data': True,
    'install_requires': [],  
    'tests_require': ['nose', 'jinja2'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'roll',
    'author_email': 'roll@respect31.com',
    'classifiers': ['Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],       
    'description': 'Box is a library to provide common functionality.',
    'download_url':'https://github.com/respect31/box/tarball/0.31.0',
    'license': 'MIT License',
    'maintainer': 'roll',
    'maintainer_email': 'roll@respect31.com',
    'platforms': ['Unix'],
    'url': 'https://github.com/respect31/box',
    'long_description': '''.. DO NOT CHANGE THIS FILE. SOURCE IS IN "_sources" DIRECTORY.

Box
=====================
Box is a library to provide common functionality.

.. image:: http://img.shields.io/badge/code-GitHub-brightgreen.svg
     :target: https://github.com/respect31/box
     :alt: code
.. image:: http://img.shields.io/travis/respect31/box/master.svg
     :target: https://travis-ci.org/respect31/box 
     :alt: build
.. image:: http://img.shields.io/coveralls/respect31/box/master.svg 
     :target: https://coveralls.io/r/respect31/box  
     :alt: coverage
.. image:: http://img.shields.io/badge/docs-RTD-brightgreen.svg
     :target: http://box.readthedocs.org
     :alt: docs     
.. image:: http://img.shields.io/pypi/v/box.svg
     :target: https://pypi.python.org/pypi?:action=display&name=box
     :alt: pypi

*Package is under active development. Before version 1 backward-compatibility 
on minor releases (0.x.0), documentation and changelog are not guaranteed.*

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install box

Authors
-------
- roll <roll@respect31.com>

Maintainers
-----------
- roll <roll@respect31.com>

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

if (not os.environ.get('TRAVIS', None) and  
	not	os.environ.get('READTHEDOCS', None)):
	package['entry_points'] = {}
	package['data_files'] = []

if __name__ == '__main__':
	from setuptools import setup
	setup(**package)