class setup:
    """Decorate method to be added to sphinx setup.
    """
    
    #Public
        
    def __call__(self, method):
        self._method = method
        return self
    
    def invoke(self, app):
        self._method(app)