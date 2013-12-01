from django.http import HttpResponse
from lib31.django import Handler
from .exceptions import BadRequest
from .formatter import ProxyFormatter
from .request import Request
from .responder import ProxyResponder

class Handler(Handler):
    
    #Public
    
    def __init__(self, http_request, version, format, resource, constraints=''):
        self._request = self._request_class(http_request, version, 
                                            format, resource, constraints)
                           
    #TODO: reimpl!!!
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
    def _responder_class(self):
        return ProxyResponder
    
    @property
    def _formatter_class(self):
        return ProxyFormatter