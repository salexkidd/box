from run import FindModule
from packgram import ManageModule
    
class MainModule(ManageModule):
    
    #Modules
        
    #TODO: move to ManageModule when deferred load will be added to run   
    #TODO: use names instead basedir after run fix
    docs = FindModule(basedir='docs')
    tests = FindModule(basedir='tests')    
        
    #Vars
    
    author = 'roll'
    author_email = 'roll@respect31.com'
    classifiers = [
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3', 
        'Topic :: Software Development :: Libraries :: Python Modules', 
        'Topic :: System :: Systems Administration',
    ]
    description = 'Box is a library to provide common functionality.'
    development_requires = ['packgram>=0.10.3', 'sphinx', 'sphinx_rtd_theme']   
    github_user = 'respect31'
    install_requires = []
    license = 'MIT License'
    name = 'box'
    platforms = ['Unix']
    pypi_password_secure = 'jFRWJAyhP5RA9j8CEpJzwJhwZmbfcxW1HpRO43mMu2/Nh3FW7GdisUovCLOS/khygJvh86vfe6m69+GEVuH/VgUEw8GcdZ41Zcla0ZnBhQrH0PTQel5Fou85foD7yXf42toVY3DV7C/JPk8PK3swSlIJ26n4dVreI7y1xvRmVHk='
    tests_require = ['nose', 'jinja2']
    test_suite = 'nose.collector'
