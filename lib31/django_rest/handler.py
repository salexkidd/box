from django.http import HttpResponse
from lib31.django import Handler
from .presenter import MappingPresenter
from .responder import MappingResponder
from .exceptions import BadRequest, FormatIsNotSuppported

class Handler(Handler):
    
    #Public
    
    def handle(self, http_request, url_request):
        self._request = self._request_class(http_request, version, 
                                            format, resource, constraints)
        try:
            responder = self._responder_class(self._request)
            response = responder.respond()
        except BadRequest:
            pass
        try:
            formatter = self._formatter_class(response)
            text = formatter.format()
        except FormatIsNotSuppported:
            pass
        return HttpResponse(text)
    
    #Protected
    
    @property
    def _presenter_class(self):
        return MappingPresenter    
    
    @property
    def _responder_class(self):
        return MappingResponder