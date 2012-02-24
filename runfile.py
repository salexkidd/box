from package import Package
from lib31.decorators import cachedproperty
from runclasses.program import ProgramRunclass

class Runclass(ProgramRunclass):
    
    @cachedproperty
    def package(self):
        return Package()