from abc import ABCMeta, abstractmethod

class Function(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        function = object.__new__(self)
        function.__init__(*args, **kwargs)
        result = function.__call__()
        return result


class FunctionCall(metaclass=Function):

    #Public
    
    @abstractmethod    
    def __call__(self):
        pass #pragma: no cover