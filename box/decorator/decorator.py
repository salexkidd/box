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
    
    If Decorator implementation doesn't override __init__ method
    it works as decorator without arguments:: 
    
      class decorator(Decorator):
          def __call__(self, function):
              return function
              
      @decorator
      def function(self):
          pass
              
    Otherwise it accepts arguments and calls __init__ with it::
    
      class decorator(Decorator):
          def __init__(self, param):
              self._param = param
          def __call__(self, function):
              print(self._param)
              return function
              
      @decorator('param')
      def function(self):
          pass              
    """
    
    #Public
    
    @abstractmethod
    def __call__(self, function):
        pass #pragma: no cover        