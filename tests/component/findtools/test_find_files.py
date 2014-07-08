import re
import unittest
from unittest.mock import patch
from box.findtools.find_files import find_files, FilepathConstraint

class find_files_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.filepathes = [
            'file1', 'file2', 'dir/file1', 'dir/file2', 'dir/subdir/file3']
        self.patcher = patch.object(
            FilepathConstraint, 'inner_filepathes', self.filepathes)
        self.patcher.start()
        self.addCleanup(patch.stopall) 
        
    def test(self):
        files = list(find_files(
            filepath='file*',
            basedir='basedir'))
        self.assertEqual(files, ['file1', 'file2'])
     
    def test_with_filename(self):
        files = list(find_files(filename='file3'))
        self.assertEqual(files, ['dir/subdir/file3'])        
        
    def test_with_filename_is_regex(self):
        filename = re.compile('file1+')
        files = list(find_files(filename=filename, maxdepth=1))
        self.assertEqual(files, ['file1'])     
    
    def test_with_filepath(self):
        files = list(find_files(filepath='file*'))
        self.assertEqual(files, ['file1', 'file2']) 
         
    def test_with_filepath_is_regex(self):
        filepath = re.compile('.*2$')
        files = list(find_files(filepath=filepath))
        self.assertEqual(files, ['file2', 'dir/file2']) 
    
    def test_with_basedir(self):
        files = list(find_files(filename='file3', basedir='basedir'))
        self.assertEqual(files, ['dir/subdir/file3'])
        
    def test_with_basedir_and_join(self):
        files = list(find_files(filename='file3', basedir='basedir', join=True))
        self.assertEqual(files, ['basedir/dir/subdir/file3'])        
        
    def test_with_maxdepth_is_1(self):
        files = list(find_files(filename='file1', maxdepth=1))
        self.assertEqual(files, ['file1'])
        
    def test_with_maxdepth_is_2(self):
        files = list(find_files(filename='file1', maxdepth=2))
        self.assertEqual(files, ['file1', 'dir/file1'])
        
    def test_with_mapper(self):
        mapper = lambda emitter: emitter.value(emitter.value()+'!')
        files = list(find_files(filename='file1', mappers=[mapper]))
        self.assertEqual(files, ['file1!', 'dir/file1!'])         
          
    def test_with_reducer(self):
        reducer=lambda files: list(files)[0]
        files = find_files(filename='file1', maxdepth=1, reducers=[reducer])
        self.assertEqual(files, 'file1')
    
    def test_with_reducer_and_fallback(self):
        reducer = lambda values: 1/0
        files = find_files(reducers=[reducer], fallback='fallback')
        self.assertEqual(files, 'fallback')