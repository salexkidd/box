import os
from setuptools import find_packages, setup

setup(

	#Main
	
    name='lib31',
	version='0.7.0',
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
    download_url='https://github.com/respect31/lib31/tarball/1.version_level.0.7.0.0.0.0',    
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules'],    
    description='Lib31 is library to provide common functionality.',    
    long_description='''Lib31
=====
Lib31 is library to provide common functionality.

|build| |coverage| |version| |downloads| |licence|

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
- removed python.import_*

0.5.0
`````
- ported to Python 3.3 without previous version support
- updated application programing interface

.. |build| image:: https://secure.travis-ci.org/respect31/lib31.png?branch=master 
             :target: https://travis-ci.org/respect31/lib31 
             :alt: Build
.. |coverage| image:: https://coveralls.io/repos/respect31/lib31/badge.png?branch=master 
                :target: https://coveralls.io/r/respect31/lib31  
                :alt: Coverage  
.. |version| image:: https://pypip.in/v/lib31/badge.png 
               :target: https://pypi.python.org/pypi/lib31/ 
               :alt: Version
.. |downloads| image:: https://pypip.in/d/lib31/badge.png 
                 :target: https://pypi.python.org/pypi/lib31/ 
                 :alt: Downloads
.. |licence| image:: https://pypip.in/license/lib31/badge.png 
               :target: https://pypi.python.org/pypi/lib31/ 
               :alt: License''',
        
)