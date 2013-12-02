from django.conf.urls import include
from .binding import HandlerBinding, IncludeBinding

class Dispatcher:
    
    #Public
    
    def __init__(self):
        self._bindings = []
    
    def bind(self, regex, handler, name=None):
        self._bindings.append(
            HandlerBinding(regex, handler, name=name)
        )
        
    def include(self, regex, urls, namespace=None, app_name=None):
        self._bindings.append(
            IncludeBinding(regex, include(urls, namespace, app_name))
        )
        
    def export(self, scope):
        patterns = []
        for binding in self._bindings:
            patterns.append(binding.pattern)
        scope['urlpatterns'] = patterns
        
