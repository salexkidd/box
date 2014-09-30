from ..functools import Decorator


class setup(Decorator):
    """Decorate method to be added to sphinx setup.
    """

    # Public

    decorator = '_box_sphinx_setup'

    def __call__(self, function):
        setattr(function, self.decorator, self)
        return function

    def invoke(self, function, app):
        function(app)
