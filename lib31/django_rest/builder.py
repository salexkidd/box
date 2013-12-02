import json
from abc import ABCMeta, abstractmethod
from lib31.json import DateEncoder

class Builder(metaclass=ABCMeta):
    
    @abstractmethod
    def build(self, response):
        pass #pragma: no cover
        
    @property
    def _response_dict(self):
        return {'result': self._response.result,
                'error': self._response.error}
    

class JSONBuilder(Builder):
    
    #Public
    
    def format(self):
        return json.dumps(self._response_dict, cls=DateEncoder)