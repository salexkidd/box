from ..collections import merge_dicts

class ColoredPrint:
    """Wrap print function to work with styles.
    """

    # Public

    print = staticmethod(print)

    # Codes

    codes = {
        'begin': '\x1b[',
        'separator': ';',
        'end': 'm',
    }

    # Offsets

    offsets = {
        'bold': 1,
        'dark': 2,
        'underline': 4,
        'blink': 5,
        'reverse': 7,
        'concealed': 8 ,
        'foreground': 30,
        'background': 40,
        'bright': 30,
    }

    # Colors offsets

    color_offsets = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
        'default': 9,
    }

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            attr = getattr(self, key, None)
            if isinstance(attr, dict):
                value = merge_dicts(attr, value)
            setattr(self, key, value)
        self._stack = []

    def __enter__(self):
        # Set style
        if self._stack:
            code = self._stack[-1:]
            self.print(code)
        return self

    def __exit__(self, cls, value, traceback):
        # Reset style
        code = self._make_code()
        self.print(code)
        # Recover style
        self._stack.pop()
        for code in self._stack:
            self.print(code)

    def __call__(self, *args, **kwargs):
        return self.print(*args, **kwargs)

    def style(self, **kwargs):
        offsets = []
        for key, value in kwargs.items():
            if value is True:
                offset = self.offsets[key]
            elif value:
                offset = self.offsets[key] + self.color_offsets[value]
            offsets.append(offset)
        code = self._make_code(offsets)
        self._stack.append(code)
        return self

    # Protected

    def _make_code(self, offsets=None):
        if offsets is None:
            offsets = []
        style_code = self.codes['separator'].join(map(str, offsets))
        code = self.codes['begin'] + style_code + self.codes['end']
        return code
