from package import Package
from runclasses.program import ProgramRunclass
from lib31.decorators.cachedproperty import cachedproperty

class Runclass(ProgramRunclass):
    
    @cachedproperty
    def _package(self):
        return Package()