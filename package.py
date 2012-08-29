from box import Package

class Package(Package):

    #Public
    
    name = 'lib31'
    install_requires = ['box>=0.3']
    test_suite = 'nose.collector'
    tests_require = ['nose']
    
    platforms=['Unix', 'POSIX']   
    classifiers=[
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
    
    
package = Package()