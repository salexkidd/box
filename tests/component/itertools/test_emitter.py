import unittest
from box.itertools.map_reduce import Emitter

class EmitterTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.emitter = Emitter('value', attr='attr')

    def test___getattr__(self):
        self.assertEqual(self.emitter.attr, 'attr')

    def test___getattr___not_existent(self):
        self.assertRaises(AttributeError,
            getattr, self.emitter, 'not_existent')

    def test_value(self):
        self.assertEqual(self.emitter.value(), 'value')

    def test_value_set(self):
        self.assertEqual(self.emitter.value('new_value'), self.emitter)
        self.assertEqual(self.emitter.value(), 'new_value')

    def test_value_set_with_condition_is_false(self):
        self.assertEqual(self.emitter.value('new_value', False), self.emitter)
        self.assertEqual(self.emitter.value(), 'value')

    def test_emit(self):
        self.assertEqual(self.emitter.emit('new_value'), self.emitter)
        self.assertEqual(self.emitter.emitted, ['new_value'])

    def test_emit_with_condition_is_false(self):
        self.assertEqual(self.emitter.emit('new_value', False), self.emitter)
        self.assertEqual(self.emitter.emitted, [])

    def test_skip(self):
        self.assertEqual(self.emitter.skip(), self.emitter)
        self.assertEqual(self.emitter.skipped, True)

    def test_skip_with_condition_is_false(self):
        self.assertEqual(self.emitter.skip(False), self.emitter)
        self.assertEqual(self.emitter.skipped, False)

    def test_stop(self):
        self.assertEqual(self.emitter.stop(), self.emitter)
        self.assertEqual(self.emitter.stopped, True)

    def test_stop_with_condition_is_false(self):
        self.assertEqual(self.emitter.stop(False), self.emitter)
        self.assertEqual(self.emitter.stopped, False)

    def test_stop_with_if_not_skipped_is_true(self):
        self.assertEqual(self.emitter.stop(if_not_skipped=True), self.emitter)
        self.assertEqual(self.emitter.stopped, True)

    def test_stop_with_if_not_skipped_is_true_and_skipped(self):
        self.assertEqual(self.emitter.skip(), self.emitter)
        self.assertEqual(self.emitter.stop(if_not_skipped=True), self.emitter)
        self.assertEqual(self.emitter.stopped, False)

    def test_emitted(self):
        self.assertEqual(self.emitter.emitted, [])

    def test_stopped(self):
        self.assertEqual(self.emitter.stopped, False)

    def test_skipped(self):
        self.assertEqual(self.emitter.skipped, False)
