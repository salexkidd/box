from box import Package, CommonPackageMixin, ReStructuredPackageMixin

class Package(CommonPackageMixin,
              ReStructuredPackageMixin,
              Package):

    #Public
    
    install_requires = ['box>=0.7']
    test_suite = 'nose.collector'
    tests_require = ['nose']    
    
package = Package()