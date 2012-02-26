from lib31.decorators.cachedproperty import cachedproperty
from runclasses.program import ProgramRunclass
from package import Package

class Runclass(ProgramRunclass):
    
    def register(self):
        pass
    
    @cachedproperty
    def _package(self):
        return Package()