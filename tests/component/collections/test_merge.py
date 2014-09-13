import unittest
import operator
from box.collections.merge import merge_dicts


class merge_dicts_Test(unittest.TestCase):

    # Public

    def test(self):
        self.assertEqual(
            merge_dicts(
                {'a': 1},
                {'b': 2}),
            {'a': 1, 'b': 2})

    def test_nested(self):
        self.assertEqual(
            merge_dicts(
                {'a': 1, 'b': {'b1': 1, 'b2': 2}},
                {'a': 2, 'b': {'b2': 1, 'b3': 2}}),
            {'a': 2, 'b': {'b1': 1, 'b2': 1, 'b3': 2}})

    def test_list_resolver(self):
        self.assertEqual(
            merge_dicts(
                {'a': 1, 'b': [1, 2]},
                {'a': 2, 'b': [3]},
                resolvers={list: operator.add}),
            {'a': 2, 'b': [1, 2, 3]})

    def test_int_and_float_resolver(self):
        self.assertEqual(
            merge_dicts(
                {'a': 1, 'b': 3.0},
                {'a': 2.0, 'b': 4},
                resolvers={int: operator.mul, float: operator.mul}),
            {'a': 2.0, 'b': 12.0})
