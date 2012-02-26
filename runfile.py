from runclasses.package import PackageRunclass
from package import Package

class Runclass(PackageRunclass):
    
    PACKAGE = Package
    
    def register(self):
        pass