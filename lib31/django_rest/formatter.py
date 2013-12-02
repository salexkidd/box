import json
from abc import ABCMeta, abstractmethod
from lib31.json import DateEncoder
from .exceptions import FormatIsNotSuppported

class Formatter(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, response):
        self._response = response
        
    @abstractmethod
    def format(self):
        pass #pragma: no cover
    
    #Protected
    
    @property
    def _response_dict(self):
        return {'result': self._response.result,
                'error': self._response.error}
    

class JSONFormatter(Formatter):
    
    #Public
    
    def format(self):
        return json.dumps(self._response_dict, cls=DateEncoder)


class MappingFormatter(Formatter):

    #Protected
    
    _formatter_classes = {
        'json': JSONFormatter,
    }
    _formatter_packages = []   