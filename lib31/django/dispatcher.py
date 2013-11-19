from django.conf.urls.defaults import include
from .binding import HandlerBinding, IncludeBinding

class Dispatcher(object):
    
    #Public
    
    def __init__(self):
        self.__bindings = []
    
    def bind(self, regex, handler, name=None):
        self.__bindings.append(
            HandlerBinding(regex, handler, name=name)
        )
        
    def include(self, regex, urls, namespace=None, app_name=None):
        self.__bindings.append(
            IncludeBinding(regex, include(urls, namespace, app_name))
        )
        
    def export(self, scope):
        patterns = []
        for binding in self.__bindings:
            patterns.append(binding.pattern)
        scope['urlpatterns'] = patterns
        
