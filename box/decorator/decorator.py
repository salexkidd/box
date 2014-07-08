from abc import ABCMeta, abstractmethod

class DecoratorMetaclass(ABCMeta):
    """Metaclass to unify 1-2 step decorators implimentation.
    """
    
    #Public
    
    def __call__(self, *args, **kwargs):
        decorator = object.__new__(self)
        if getattr(self, '__init__') is object.__init__:
            #Init is not provided - 1 step
            return decorator.__call__(*args, **kwargs)            
        else:
            #Init is provided - 2 steps 
            decorator.__init__(*args, **kwargs)
            return decorator
    
    def __instancecheck__(self, instance):
        result = issubclass(instance, self)
        if not result:
            result = super().__instancecheck__(instance)
        return result
        
        
class Decorator(metaclass=DecoratorMetaclass):
    """Base abstract class for unified 1-2 step decorators.
    """
    
    #Public
    
    @abstractmethod
    def __call__(self, obj):
        pass #pragma: no cover        