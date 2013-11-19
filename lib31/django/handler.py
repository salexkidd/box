from abc import ABCMeta, abstractmethod

class Handler(object):
    
    #Public
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass #pragma: no cover

    @abstractmethod
    def process(self):
        pass #pragma: no cover
    

class HandlerAdapter(object):
    
    #Public
    
    def __init__(self, handler):
        self.__handler = handler
    
    def process(self, *args, **kwargs):
        handler = self.__handler(*args, **kwargs)
        return handler.process()