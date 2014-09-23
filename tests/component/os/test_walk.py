import os
import re
import unittest
from functools import partial
from unittest.mock import patch
from importlib import import_module
component = import_module('box.os.walk')


class walk_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        patch.object(component.os, 'listdir', new=self.mock_listdir).start()
        patch.object(component.os.path, 'islink', new=self.mock_islink).start()
        patch.object(component.os.path, 'isfile', new=self.mock_isfile).start()
        patch.object(component.os.path, 'isdir', new=self.mock_isdir).start()
        self.error = os.error()
        self.pwalk = partial(component.enhanced_walk, sorter=sorted)

    # Helpers

    def mock_listdir(self, path):
        if path == '.':
            return ['dir1', 'dir2', 'file1', 'file2', 'link']
        elif path == 'dir1':
            return ['subdir1', 'file1', ]
        elif path == 'dir2':
            return ['file1', ]
        elif path == 'dir1/subdir1':
            return ['file1']
        elif path == 'error':
            raise self.error

    def mock_islink(self, path):
        return bool(re.search('link\d?$', path))

    def mock_isfile(self, path):
        return bool(re.search('file\d?$', path))

    def mock_isdir(self, path):
        return bool(re.search('dir\d?$', path))

    # Tests

    def test(self):
        levels = list(self.pwalk())
        self.assertEqual(len(levels), 3)
        self.assertEqual(levels[0],
            (# Dirpathes
             ['dir1',
              'dir2'],
             # Filepathes
             ['file1',
              'file2']))
        self.assertEqual(levels[1],
            (# Dirpathes
             ['dir1/subdir1'],
             # Filepathes
             ['dir1/file1',
              'dir2/file1']))
        self.assertEqual(levels[2],
            (# Dirpathes
             [],
             # Filepathes
             ['dir1/subdir1/file1']))

    def test_with_dirpath(self):
        levels = list(self.pwalk('dir1'))
        self.assertEqual(len(levels), 2)
        self.assertEqual(levels[0],
            (# Dirpathes
             ['dir1/subdir1'],
             # Filepathes
             ['dir1/file1']))
        self.assertEqual(levels[1],
            (# Dirpathes
             [],
             # Filepathes
             ['dir1/subdir1/file1']))

    def test_with_basedir(self):
        levels = list(self.pwalk(basedir='dir1'))
        self.assertEqual(len(levels), 2)
        self.assertEqual(levels[0],
            (# Dirpathes
             ['subdir1'],
             # Filepathes
             ['file1']))
        self.assertEqual(levels[1],
            (# Dirpathes
             [],
             # Filepathes
             ['subdir1/file1']))

    def test_with_dirpath_and_basedir(self):
        levels = list(self.pwalk('subdir1', basedir='dir1'))
        self.assertEqual(len(levels), 1)
        self.assertEqual(levels[0],
            (# Dirpathes
             [],
             # Filepathes
             ['subdir1/file1']))

    def test_with_mode_is_files(self):
        files = list(self.pwalk(mode='files'))
        self.assertEqual(files, [
            # Filepathes
            'file1',
            'file2',
            'dir1/file1',
            'dir2/file1',
            'dir1/subdir1/file1'])

    def test_with_mode_is_dirs(self):
        files = list(self.pwalk(mode='dirs'))
        self.assertEqual(files, [
            # Dirpathes
            'dir1',
            'dir2',
            'dir1/subdir1'])
