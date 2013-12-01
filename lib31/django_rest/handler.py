from abc import ABCMeta, abstractmethod
from django.http import HttpResponse
from lib31.django import Handler
from lib31.python import cachedproperty
from .exceptions import BadRequest
from .parser import Parser

class Handler(Handler, metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, request, version, format, resource, constraints=''):
        self._requst = request
        self._version = version
        self._format = format
        self._resource = resource
        self._constraints = constraints
                           
    #TODO: impl raise
    def handle(self):
        struct = {}
        try:
            struct['data'] = self._responder.process()
        except BadRequest as exception:
            struct['error'] = True
            struct['message'] = exception.message
        text = self._formatter.process(struct)
        return HttpResponse(text)
    
    #Protected
    
    @property
    @abstractmethod
    def _responder(self):
        pass #pragma: no cover
    
    @property
    @abstractmethod
    def _formatter(self):
        pass #pragma: no cover
        
    @cachedproperty
    def _parsed_constraints(self):
        return self._parser.process(self._constraints)
    
    @cachedproperty
    def _parser(self):
        return Parser()