from abc import ABCMeta, abstractmethod
from django.http import HttpResponse
from lib31.django import Handler
from .exceptions import BadRequest
from .formatter import JSONFormatter
from .request import Request

class Handler(Handler, metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, http_request, version, format, resource, constraints=''):
        self._request = self._request_class(http_request, version, 
                                            format, resource, constraints)
                           
    #TODO: impl raise
    def handle(self):
        respond = {}
        try:
            respond['data'] = self._responder.respond(self._parsed_constraints)
        except BadRequest as exception:
            respond['error'] = True
            respond['message'] = exception.message
        text = self._formatter.format(respond)
        return HttpResponse(text)
    
    #Protected
    
    @property
    def _request_class(self):
        return Request
    
    @property
    @abstractmethod
    def _responder_class(self):
        pass #pragma: no cover
    
    @property
    def _formatter_class(self):
        return JSONFormatter