from argparse import ArgumentParser


class Parser(ArgumentParser):
    """ArgumentParser optionally uses exception instead of exit."""

    # Public

    def __init__(self, *args, exception=None, **kwargs):
        self.__exception = exception
        super().__init__(*args, **kwargs)

    def error(self, message):
        if self.__exception:
            raise self.__exception(message)
        else:
            super().error(message)
