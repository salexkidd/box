import re
import unittest
from importlib import import_module
component = import_module('box.types.regex')


class RegexCompiledPatternTypeTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertEqual(
            component.RegexCompiledPatternType, type(re.compile('')))
