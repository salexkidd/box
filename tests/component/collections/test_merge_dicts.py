import unittest
from box.collections.merge_dicts import merge_dicts

class merge_dicts_Test(unittest.TestCase):

    #Public

    def test(self):
        result = merge_dicts({'a': 1}, {'b': 2})
        self.assertEqual(result, {'a': 1, 'b': 2})