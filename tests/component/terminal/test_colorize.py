import unittest
from box.terminal.colorize import Colorize


class ColorizeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.colorize = Colorize()

    def test(self):
        with self.colorize(foreground='red', background='white'):
            string1 = self.colorize('string1')
            with self.colorize(background='green'):
                string2 = self.colorize('string2')
            string3 = self.colorize('string3', background='green')
        self.assertEqual(string1, '\x1b[31;47mstring1\x1b[m')
        self.assertEqual(string2, '\x1b[31;47m\x1b[42mstring2\x1b[m')
        self.assertEqual(string3, '\x1b[31;47m\x1b[42mstring3\x1b[m')
