from django.http import HttpResponse
from lib31.django import Handler
from .presenter import MappingPresenter
from .responder import MappingResponder

class Handler(Handler):
    
    #Public
    
    def handle(self, http_request, url_request):
        self._presenter = self._presenter_class()
        responder = self._responder_class(self._request)
        response = responder.respond()
        formatter = self._formatter_class(response)
        text = formatter.format()
        return HttpResponse(text)
    
    #Protected
    
    @property
    def _presenter_class(self):
        return MappingPresenter    
    
    @property
    def _responder_class(self):
        return MappingResponder