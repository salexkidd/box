import os
import pprint
import unittest
from lib31.reader import Reader
from lib31.package import Package
from lib31.decorators.cachedproperty import cachedproperty

#Fixtures
class PackageImp(Package):
    
    NAME = 'name'
    URL = 'url'

    @cachedproperty       
    def _reader(self):
        return Reader(os.path.dirname(__file__), '..')


#Tests
class PackageTest(unittest.TestCase):
    
    def setUp(self):
        self.package = PackageImp()
    
    def test(self):
        pprint.pprint(self.package)