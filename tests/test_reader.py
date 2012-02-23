import os
import unittest
from lib31.reader import Reader

class ReaderTest(unittest.TestCase):
    
    FILENAME = 'test_reader.py'

    def setUp(self):
        self.reader = Reader(os.path.dirname(__file__))

    def test_read(self):
        self.assertTrue(self.reader.read(self.FILENAME).
                        startswith('import'))
        
    def test_path(self):
        self.assertEqual(self.reader.path(self.FILENAME),
                         self.filepath)
      
    @property
    def filepath(self):
        return os.path.join(os.path.dirname(__file__), self.FILENAME)