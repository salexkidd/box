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
            self.cprint('test')
            with self.cprint.style(background='green'):
                self.cprint('test2')
        # Check print call
        self.print.assert_has_calls([
            call('\x1b[31;47m'),
            call('test'),
            call('\x1b[42m'),
            call('test2'),
            call('\x1b[m'),
            call('\x1b[m')])
