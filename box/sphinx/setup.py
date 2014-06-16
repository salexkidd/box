from ..decorator import Decorator

class setup(Decorator):
    """Decorate method to be added to sphinx setup.
    """
    
    #Public
    
    def __call__(self, method):
        self._method = method
        method._box_sphinx_setup = self
        return method
        
    def invoke(self, app):
        self._method(app)