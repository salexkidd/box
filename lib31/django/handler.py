from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def __init__(self, request, *args, **kwargs):
        pass #pragma: no cover

    @abstractmethod
    def handle(self):
        pass #pragma: no cover
    

class HandlerAdapter:
    
    #Public
    
    def __init__(self, handler_class):
        self._handler_class = handler_class
    
    def handle(self, request, *args, **kwargs):
        handler = self._handler_class(request, *args, **kwargs)
        return handler.handle()