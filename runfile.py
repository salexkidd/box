from package import Package
from lib31.runclass import ProgramRunclass
from lib31.property import cachedproperty

class Runclass(ProgramRunclass):
    
    @cachedproperty
    def package(self):
        return Package()