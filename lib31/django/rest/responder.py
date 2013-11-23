from abc import ABCMeta, abstractmethod
from .exceptions import ConstraintsAreNotSuppported

class Responder(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, constraints={}):
        if constraints:
            raise ConstraintsAreNotSuppported(constraints)
        
    def process(self):
        return {
            'keys': self._get_keys(),
            'values': self._get_values(),
        }
        
    #Protected
    
    def _get_keys(self):
        return [field.name for field in self._entity_class._meta.fields]
        
    def _get_values(self):
        return list(self._entity_class.query.values_list())
    
    @property
    @abstractmethod
    def _entity_class(self):
        pass #pragma: no cover    