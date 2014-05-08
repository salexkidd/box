import re
import unittest
from unittest.mock import Mock
from box.findtools.find_files import find_files

class find_files_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        filepathes = [
            'file1', 'file2', 'dir/file1', 'dir/file2', 'dir/subdir/file3']
        self.find = self._make_mock_find(filepathes)
   
    def test(self):
        files = list(self.find(
            basedir='basedir',
            onwalkerror='onwalkerror'))
        self.assertEqual(len(files), 5)
        self.find._walk.assert_called_with(
            basedir='basedir',
            sorter=sorted,
            mode='files',
            onerror='onwalkerror')      
        
    def test_with_maxdepth_is_1(self):
        files = list(self.find(filename='file1', maxdepth=1))
        self.assertEqual(files, ['file1'])
        
    def test_with_maxdepth_is_2(self):
        files = list(self.find(filename='file1', maxdepth=2))
        self.assertEqual(files, ['file1', 'dir/file1'])
     
    def test_with_filename(self):
        files = list(self.find(filename='file3'))
        self.assertEqual(files, ['dir/subdir/file3'])        
        
    def test_with_filename_is_regex(self):
        filename = re.compile('file1+')
        files = list(self.find(filename=filename, maxdepth=1))
        self.assertEqual(files, ['file1'])     
        
    def test_with_filepath_is_regex(self):
        filepath = re.compile('.*2$')
        files = list(self.find(filepath=filepath))
        self.assertEqual(files, ['file2', 'dir/file2'])        
        
    def test_with_mapper(self):
        mapper = lambda emitter: emitter.value(emitter.value()+'!')
        files = list(self.find(filename='file1', mappers=[mapper]))
        self.assertEqual(files, ['file1!', 'dir/file1!'])         
          
    def test_with_reducer(self):
        reducer=lambda files: list(files)[0]
        files = self.find(filename='file1', maxdepth=1, reducers=[reducer])
        self.assertEqual(files, 'file1')
    
    def test_with_reducer_and_fallback(self):
        reducer = lambda values: 1/0
        files = self.find(reducers=[reducer], fallback='fallback')
        self.assertEqual(files, 'fallback')                     
    
    #Protected
    
    def _make_mock_find(self, filepathes):
        class mock_find(find_files):
            #Protected
            _walk = Mock(return_value=filepathes)
            _glob = Mock(return_value=filepathes)
        return mock_find