from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def __init__(self):
        pass #pragma: no cover

    @abstractmethod
    def handle(self):
        pass #pragma: no cover
    

class HandlerAdapter:
    
    #Public
    
    def __init__(self, handler):
        self.__handler = handler
    
    def handle(self, *args, **kwargs):
        handler = self.__handler(*args, **kwargs)
        return handler.process()