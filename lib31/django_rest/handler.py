from django.http import HttpResponse
from lib31.django import Handler
from .formatter import MappingFormatter
from .request import Request
from .responder import MappingResponder

class Handler(Handler):
    
    #Public
    
    def __init__(self, http_request, version, format, resource, constraints=''):
        self._request = self._request_class(http_request, version, 
                                            format, resource, constraints)
                           
    def handle(self):
        responder = self._responder_class(self._request)
        response = responder.respond()
        formatter = self._formatter_class(response)
        text = formatter.format()
        return HttpResponse(text)
    
    #Protected
    
    @property
    def _request_class(self):
        return Request
    
    @property
    def _responder_class(self):
        return MappingResponder
    
    @property
    def _formatter_class(self):
        return MappingFormatter