class Response:
    
    #Public
    
    def __init__(self, result, error=False):
        self._result = result
        self._error = error
      
    @property    
    def result(self):
        self._result
      
    @property    
    def error(self):
        self._error