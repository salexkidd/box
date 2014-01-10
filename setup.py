import os
from setuptools import find_packages, setup

setup(

	#Main

    name='box',
	version='None',
	packages=find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	include_package_data=True,
    tests_require=['nose'],
    test_suite='nose.collector',
    
    #Description
    
    author='None',
    author_email='None',
    maintainer='None',
    maintainer_email='None',
    license='None',    
    url='https://github.com/none/box',
    download_url='https://github.com/none/box/tarball/none',    
    classifiers=[],    
    description='Box is library to provide common functionality.',    
    long_description='''Box
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
- Respect31 <post@respect31.com>
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
        
)