from abc import ABCMeta, abstractproperty
from django.conf.urls import url
from .handler import Handler

class BaseBinding(metaclass=ABCMeta):
    
    #Public
    
    @property    
    def pattern(self):
        return url(self._regex, self._handler, 
                   name=self._name, **self._params)
        
    #Protected   
        
    @abstractproperty
    def _handler(self):
        pass #pragma: no cover
        
        
class HandlerBinding(BaseBinding):
    
    #Public
    
    def __init__(self, regex, handler, name=None, **params):
        self._regex = regex
        self._name = name
        self._params = params
        self._handler = Handler(handler)
    
    
class IncludeBinding(BaseBinding):
    
    #Public
    
    def __init__(self, regex, include, name=None, **params):
        self._regex = regex
        self._name = name
        self._params = params
        self._include = include
            
    #Protected   
   
    @property 
    def _handler(self):
        return self._include        