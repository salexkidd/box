import os
from setuptools import find_packages, setup

package = {}

setup(

	#Main
	
    name='lib31',
	version='0.7.3',
	packages=find_packages(os.path.dirname(__file__) or '.', exclude=['tests*']),
	include_package_data=True,
    tests_require=['nose'],
    test_suite='nose.collector',
    
    #Description
    
    author='Respect31',
    author_email='post@respect31.com',
    maintainer='Respect31',
    maintainer_email='post@respect31.com',
    license='MIT License',    
    url='https://github.com/respect31/lib31',
    download_url='https://github.com/respect31/lib31/tarball/0.7.3',    
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules'],    
    description='Lib31 is library to provide common functionality.',    
    long_description='''Lib31
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

Classifiers
-----------
- Development Status :: 3 - Alpha
- Intended Audience :: Developers
- License :: OSI Approved :: MIT License
- Programming Language :: Python :: 3.3
- Topic :: Software Development :: Libraries :: Python Modules

History
-------
0.7.0
`````
- removed xmlrpc
- added python.ObjectLoader

0.6.0
`````
- removed python.import_*''',
        
)