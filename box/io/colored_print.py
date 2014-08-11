class ColoredPrint:
    """Wrap print function to work with styles.
    """

    # Public

    print = staticmethod(print)

    # Codes

    begin_code = '\x1b['
    separator_code = ';'
    end_code = 'm'

    # Base offsets

    foreground_offset = 30
    background_offset = 40
    bright_offset = 30

    # Color offsets

    black_offset = 0
    red_offset = 1
    green_offset = 2
    yellow_offset = 3
    blue_offset = 4
    magenta_offset = 5
    cyan_offset = 6
    white_offset = 7
    default_offset = 9

    # Formatting offsets

    bold_offset = 1
    dark_offset = 2
    underline_offset = 4
    blink_offset = 5
    reverse_offset = 7
    concealed_offset = 8

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self._stack = []

    def __enter__(self):
        code = self._stack.pop()
        self.print(code)
        return self

    def __exit__(self, cls, value, traceback):
        # Reset all
        code = self.begin_code + self.end_code
        self.print(code)

    def __call__(self, *args, **kwargs):
        return self.print(*args, **kwargs)

    def style(self, foreground=None, background=None):
        offsets = []
        if foreground is not None:
            color_offset = getattr(self, foreground + '_offset')
            offset = self.foreground_offset + color_offset
            offsets.append(offset)
        if background is not None:
            color_offset = getattr(self, background + '_offset')
            offset = self.background_offset + color_offset
            offsets.append(offset)
        style_code = self.separator_code.join(map(str, offsets))
        code = self.begin_code + style_code + self.end_code
        self._stack.append(code)
        return self
