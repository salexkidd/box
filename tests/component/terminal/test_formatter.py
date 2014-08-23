import unittest
from box.terminal.formatter import Formatter


class FormatterTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.formatter = Formatter()

    def test(self):
        with self.formatter.style(foreground='red', background='white'):
            string1 = self.formatter.format('string1')
            with self.formatter.style(background='green'):
                string2 = self.formatter.format('string2')
            string3 = self.formatter.format('string3', background='green')
        self.assertEqual(string1, '\x1b[31;47mstring1\x1b[m')
        self.assertEqual(string2, '\x1b[31;47m\x1b[42mstring2\x1b[m')
        self.assertEqual(string3, '\x1b[31;47m\x1b[42mstring3\x1b[m')

    def test_with_param(self):
        self.formatter = Formatter(offsets={'bold': 1000})
        string = self.formatter.format('string', bold=True)
        self.assertEqual(string, '\x1b[1000mstring\x1b[m')

    def test_with_bad_param(self):
        self.assertRaises(
            ValueError, Formatter, bad_param='bad_param')

    def test_format_with_bad_param(self):
        self.assertRaises(
            ValueError, self.formatter.format, 'string', bad_param='bad_param')
