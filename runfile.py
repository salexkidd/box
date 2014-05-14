from packgram import ManageModule
    
class MainModule(ManageModule):
        
    #Vars
    
    author = 'roll'
    author_email = 'roll@respect31.com'
    caution = 'DO NOT CHANGE THIS FILE. SOURCE IS IN "_sources" DIRECTORY.'    
    classifiers = [
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.3', 
        'Topic :: Software Development :: Libraries :: Python Modules', 
        'Topic :: System :: Systems Administration', 
    ]
    description = 'Box is a library to provide common functionality.'
    development_requires = [
        'runpack>=0.14',
        'sphinx',
        'sphinx_rtd_theme',
    ]    
    github_user = 'respect31'
    install_requires = []
    license = 'MIT License'
    maintainer = 'roll'
    maintainer_email = 'roll@respect31.com'
    name = 'box'
    platforms = ['Unix']
    pypi_user = 'roll'
    pypi_password_secure = 'jFRWJAyhP5RA9j8CEpJzwJhwZmbfcxW1HpRO43mMu2/Nh3FW7GdisUovCLOS/khygJvh86vfe6m69+GEVuH/VgUEw8GcdZ41Zcla0ZnBhQrH0PTQel5Fou85foD7yXf42toVY3DV7C/JPk8PK3swSlIJ26n4dVreI7y1xvRmVHk='
    tests_require = [
        'packgram>=0.8',
        'nose',
    ]
    test_suite = 'nose.collector'