from box import Package

class Package(Package):

    #Maindata
    NAME = 'lib31'
    INSTALL_REQUIRES = ['box']
    TEST_SUITE = 'nose.collector'
    TESTS_REQUIRE = ['nose']
    
    #Metadata
    PLATFORMS=['Unix', 'POSIX']   
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