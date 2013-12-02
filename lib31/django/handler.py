from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def handle(self, request, *args, **kwargs):
        pass #pragma: no cover