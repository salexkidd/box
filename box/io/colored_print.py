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
        'bright_black': 60,
        'bright_red': 61,
        'bright_green': 62,
        'bright_yellow': 63,
        'bright_blue': 64,
        'bright_magenta': 65,
        'bright_cyan': 66,
        'bright_white': 67,
    }

    def __init__(self, **params):
        for key in list(params):
            if key in ['print', 'codes', 'offsets', 'color_offsets']:
                value = params.pop(key, None)
                if value is not None:
                    if isinstance(value, dict):
                        value = merge_dicts(getattr(self, key), value)
                setattr(self, key, value)
        self._params = params
        self._buffer = None
        self._stack = []

    def __enter__(self):
        if self._buffer is not None:
            self._stack.append(self._buffer)
        return self

    def __exit__(self, cls, value, traceback):
        self._stack.pop()

    def __call__(self, *values, **params):
        # Decorate values
        values = list(values)
        if values:
            # Apply style
            for code in reversed(self._stack):
                values[0] = code + str(values[0])
            # Reset style
            code = self._make_code()
            values[-1] = str(values[-1]) + code
        # Merge params
        params = merge_dicts(self._params, params)
        return self.print(*values, **params)

    def style(self, **params):
        offsets = []
        for key, value in params.items():
            try:
                if key in ['foreground', 'background']:
                    offset = self.offsets[key] + self.color_offsets[value]
                elif value:
                    offset = self.offsets[key]
            except (KeyError, TypeError):
                raise ValueError(
                    'Bad value "{value}" for key "{key}"'.
                    format(value=value, key=key))
            offsets.append(offset)
        code = self._make_code(offsets)
        self._buffer = code
        return self

    # Protected

    def _make_code(self, offsets=None):
        if offsets is None:
            offsets = []
        style_code = self.codes['separator'].join(map(str, sorted(offsets)))
        code = self.codes['begin'] + style_code + self.codes['end']
        return code
