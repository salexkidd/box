from box import Package, CommonPackageMixin, ReStructuredPackageMixin

class Package(CommonPackageMixin,
              ReStructuredPackageMixin,
              Package):

    #Public
    
    test_suite = 'nose.collector'
    tests_require = ['nose']    
    
package = Package()