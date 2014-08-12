import unittest
from box.terminal.colorize import Colorize


class ColorizeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.colorize = Colorize()

    def test(self):
        with self.colorize(foreground='red', background='white'):
            string1 = self.colorize('*')
            with self.colorize(background='green'):
                string2 = self.colorize('*')
            string3 = self.colorize('*', background='green')
        self.assertEqual(string1, '\x1b[31;47m*\x1b[m')
        self.assertEqual(string2, '\x1b[31;47m\x1b[42m*\x1b[m')
        self.assertEqual(string3, '\x1b[31;47m\x1b[42m*\x1b[m')
