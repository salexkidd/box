import unittest
from unittest.mock import Mock, call
from box.io.colored_print import ColoredPrint


class ColoredPrintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.print = Mock()
        self.cprint = ColoredPrint(print=self.print)

    def test(self):
        with self.cprint.style(foreground='red', background='white'):
            self.cprint('test1')
            with self.cprint.style(background='green'):
                self.cprint('test2')
            self.cprint('test3', 'test4', kwarg1='kwarg1')
        # Check print call
        self.print.assert_has_calls([
            call('\x1b[31;47mtest1\x1b[m'),
            call('\x1b[31;47m\x1b[42mtest2\x1b[m'),
            call('\x1b[31;47mtest3', 'test4\x1b[m', kwarg1='kwarg1'), ])
