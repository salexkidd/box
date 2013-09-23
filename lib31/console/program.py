from abc import ABCMeta, abstractmethod

class Program(metaclass=ABCMeta):
    
    #Public
        
    def __init__(self, argv):
        self.argv = argv
        
    @abstractmethod
    def __call__(self):
        pass #pragma: no cover               