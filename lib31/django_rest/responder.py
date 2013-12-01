from abc import ABCMeta, abstractmethod

class Responder(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, request):
        self._request = request
    
    @abstractmethod
    def respond(self):
        pass #pragma: no cover 
    

class ProxyResponder(Responder):
    
    #Public
    
    pass

    #Protected
    
    _responder_classes = {}
    _responder_packages = []