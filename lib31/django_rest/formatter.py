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


class JSONFormatter(Formatter):
    
    #Public
    
    def format(self, response):
        return json.dumps(response, cls=DateEncoder)


class ProxyFormatter(Formatter):

    #Protected
    
    _formatter_classes = {
        'json': JSONFormatter,
    }
    _formatter_packages = []    