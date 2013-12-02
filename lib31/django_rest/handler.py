from django.http import HttpResponse, Http404
from lib31.django import Handler
from .presenter import MappingPresenter
from .responder import MappingResponder
from .exceptions import FormatIsNotSuppported, VersionIsNotSuppported

class Handler(Handler):
    
    #Public
    
    def handle(self, http_request, url_request):
        presenter = self._presenter_class()
        responder = self._responder_class()
        try:
            request = presenter.parse(http_request, url_request) 
            response = responder.respond(request)
            text = presenter.build(response)
        except (VersionIsNotSuppported, FormatIsNotSuppported):
            raise Http404()
        return HttpResponse(text)
    
    #Protected
    
    @property
    def _presenter_class(self):
        return MappingPresenter    
    
    @property
    def _responder_class(self):
        return MappingResponder