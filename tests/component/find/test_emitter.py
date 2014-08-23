import unittest
from box.find.emitter import FileEmitter, ObjectEmitter

class FileEmitterTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.emitter = FileEmitter(
            'value', basedir='basedir', filepath='dir/file')

    def test_basedir(self):
        self.assertEqual(self.emitter.basedir, 'basedir')

    def test_filename(self):
        self.assertEqual(self.emitter.filename, 'file')

    def test_filepath(self):
        self.assertEqual(self.emitter.filepath, 'dir/file')


class ObjectEmitterTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.emitter = ObjectEmitter(
            'value', basedir='basedir', filepath='dir/file',
            module='module', objname='objname', objself='objself')

    def test_module(self):
        self.assertEqual(self.emitter.module, 'module')

    def test_objname(self):
        self.assertEqual(self.emitter.objname, 'objname')

    def test_objself(self):
        self.assertEqual(self.emitter.objself, 'objself')

    def test_objtype(self):
        self.assertEqual(self.emitter.objtype, str)
