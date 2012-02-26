from lib31.decorators.cachedproperty import cachedproperty
from runclasses.package import PackageRunclass
from package import Package

class Runclass(PackageRunclass):
    
    def register(self):
        pass
    
    @cachedproperty
    def _package(self):
        return Package()