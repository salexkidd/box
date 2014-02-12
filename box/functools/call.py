from abc import ABCMeta, abstractmethod

class FunctionMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        function = super().__call__(*args, **kwargs)
        result = function.invoke()
        return result


class FunctionCall(metaclass=FunctionMetaclass):

    #Public
    
    @abstractmethod    
    def invoke(self):
        pass #pragma: no cover