from django.http import HttpResponse
from lib31.django import Handler
from .presenter import MappingPresenter
from .responder import MappingResponder

class Handler(Handler):
    
    #Public
    
    def handle(self, http_request, url_request):
        presenter = self._presenter_class()
        responder = self._responder_class()        
        request = presenter.parse(http_request, url_request) 
        response = responder.respond(request)
        text = presenter.build(response)
        return HttpResponse(text)
    
    #Protected
    
    @property
    def _presenter_class(self):
        return MappingPresenter    
    
    @property
    def _responder_class(self):
        return MappingResponder