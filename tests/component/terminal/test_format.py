import unittest
from box.terminal.format import Format


class ColorizeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.format = Format()

    def test(self):
        with self.format(foreground='red', background='white'):
            string1 = self.format('string1')
            with self.format(background='green'):
                string2 = self.format('string2')
            string3 = self.format('string3', background='green')
        self.assertEqual(string1, '\x1b[31;47mstring1\x1b[m')
        self.assertEqual(string2, '\x1b[31;47m\x1b[42mstring2\x1b[m')
        self.assertEqual(string3, '\x1b[31;47m\x1b[42mstring3\x1b[m')
