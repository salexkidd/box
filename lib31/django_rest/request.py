from lib31.python import cachedproperty
from .parser import Parser

class Request:
    
    #Public
    
    def __init__(self, http_request, version, format, resource, constraints=''):
        self._http_request = http_request
        self._version = version
        self._format = format
        self._resource = resource
        self._constraints = constraints
      
    @property    
    def http_request(self):
        return self._http_request
      
    @property    
    def version(self):
        return self._version
      
    @property    
    def format(self):
        return self._format
      
    @property    
    def resource(self):
        return self._resource
      
    @property    
    def constraints(self):
        return self._constraints
                 
    @cachedproperty
    def parsed_constraints(self):
        return self._parser.process(self._constraints)
    
    #Protected
    
    @cachedproperty
    def _parser(self):
        return Parser()
        