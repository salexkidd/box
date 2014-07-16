import functools
from .setup import setup

class connect(setup):
    """Decorate method to be connected to sphinx event.
    
    :param str event: sphinx event
    """

    # Public

    def __init__(self, event):
        self._event = event

    def invoke(self, obj, app):
        app.connect(self._event, functools.partial(self._method, obj))
