import os
import unittest
from box import version
from box.python import ObjectLoader

class SetupTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        PackageObjectLoader = self._make_object_loader_class()
        self.basedir = os.path.join(os.path.dirname(__file__), '..', '..')
        self.loader = PackageObjectLoader()
        self.objects = list(self.loader.load(self.basedir, 'setup.py'))

    def test(self):
        package = self.objects[0]
        self.assertEqual(package['name'], 'box')
        self.assertEqual(package['version'], version)
        
    #Protected
    
    def _make_object_loader_class(self):
        class PackageObjectLoader(ObjectLoader):
            #Protected
            def _filter_object(self, obj, module, name):
                if not super()._filter_object(obj, module, name):
                    return False
                if name != 'package':
                    return False
                return True
        return PackageObjectLoader