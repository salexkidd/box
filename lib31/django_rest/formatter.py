import json
from abc import ABCMeta, abstractmethod
from lib31.json import DateEncoder
from .exceptions import FormatIsNotSuppported

class Formatter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def format(self):
        pass #pragma: no cover


class JSONFormatter(Formatter):
    
    #Public
    
    def format(self, response):
        return json.dumps(response, cls=DateEncoder)    