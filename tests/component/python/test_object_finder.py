import unittest
from unittest.mock import Mock, call
from box.python.object_finder import ObjectFinder

class ObjectFinderTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        MockObjectFinder = self._make_mock_object_finder_class(files)
        self.finder = MockObjectFinder()
        
    def test_find(self):
        objects = list(self.finder.find('call'))
        self.assertEqual(objects, [call, call])     
    
    #Protected

    def _make_mock_object_finder_class(self, files):
        class MockObjectFinder(ObjectFinder):
            #Protected
            _source_file_loader_class = Mock(return_value=Mock(
                load_module=Mock(return_value=unittest.mock)))
            _file_finder_class = Mock(return_value=Mock(
                find=Mock(return_value=files)))
        return MockObjectFinder