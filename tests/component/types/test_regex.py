import re
import unittest
from box.types.regex import RegexCompiledPatternType

class RegexCompiledPatternTypeTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertEqual(RegexCompiledPatternType, type(re.compile('')))
