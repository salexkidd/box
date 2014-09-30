from ..functools import Decorator


class setup(Decorator):
    """Decorate method to be added to sphinx setup.
    """

    # Public

    decorator = '_box_sphinx_setup'

    def __call__(self, method):
        self.__method = method
        setattr(method, self.decorator, self)
        return method

    def invoke(self, function, app):
        function(app)
