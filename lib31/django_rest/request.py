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
        
    @cachedproperty
    def parsed_constraints(self):
        return self._parser.process(self._constraints)
    
    #Protected
    
    @cachedproperty
    def _parser(self):
        return Parser()
        