from .setup import setup


class connect(setup):
    """Decorate method to be connected to sphinx event.

    Parameters
    ----------
    event: str
        Sphinx event.
    """

    # Public

    def __init__(self, event):
        self.__event = event

    def invoke(self, function, app):
        app.connect(self.__event, function)
