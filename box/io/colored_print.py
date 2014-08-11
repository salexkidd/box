class ColoredPrint:
    """Wrap print function to work with styles.
    """

    # Public

    def __init__(self, print_function):
        self._print = print_function

    def __enter__(self):
        pass

    def __exit__(self, cls, value, traceback):
        pass
