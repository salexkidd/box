from ..collections import merge_dicts

class Formatter:
    """Console ANSI excape charsets formatter.
    """

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
        self._make_attributes(**params)
        self._offsets_stack = []
        self._offsets = None

    def __enter__(self):
        if self._offsets is not None:
            self._offsets_stack.append(self._offsets)
            self._offsets = None
        return self

    def __exit__(self, cls, value, traceback):
        self._offsets_stack.pop()

    def format(self, string, **params):
        offsets = self._make_offsets(**params)
        stack_code = ''
        for stack_offsets in self._offsets_stack:
            stack_code += self._make_code(stack_offsets)
        place_code = ''
        if offsets:
            place_code += self._make_code(offsets)
        reset_code = self._make_code()
        result = stack_code + place_code + string + reset_code
        return result

    def style(self, **params):
        offsets = self._make_offsets(**params)
        if offsets:
            self._offsets = offsets
        return self

    # Protected

    def _make_attributes(self, **params):
        for key, value in params.items():
            if value is not None:
                try:
                    value = merge_dicts(getattr(self, key), value)
                except Exception:
                    raise ValueError(
                        'Bad value "{value}" for key "{key}"'.
                        format(value=value, key=key))
            setattr(self, key, value)

    def _make_offsets(self, **params):
        offsets = []
        for key, value in params.items():
            try:
                if key in ['foreground', 'background']:
                    offset = self.offsets[key] + self.color_offsets[value]
                elif value:
                    offset = self.offsets[key]
            except Exception:
                raise ValueError(
                    'Bad value "{value}" for key "{key}"'.
                    format(value=value, key=key))
            offsets.append(offset)
        return offsets

    def _make_code(self, offsets=None):
        if offsets is None:
            offsets = []
        style_code = self.codes['separator'].join(map(str, sorted(offsets)))
        code = self.codes['begin'] + style_code + self.codes['end']
        return code