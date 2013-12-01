import json
from abc import ABCMeta, abstractmethod
from lib31.json import DateEncoder
from .exceptions import FormatIsNotSuppported

class Formatter(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, respond):
        self._respond = respond
        
    @abstractmethod
    def format(self):
        pass #pragma: no cover


class ProxyFormatter(Formatter):
    
    #Public
    
    pass

    #Protected
    
    _formatter_classes = []


class JSONFormatter(Formatter):
    
    #Public
    
    def format(self, response):
        return json.dumps(response, cls=DateEncoder)    