import sys
from .decorators.cachedproperty import cachedproperty

class Release(object):
    
    def __init__(self, package, step, level=None):
        self.package = package
        self.step = step
        self.level = level

    def apply(self):
        for path, code in self.changes.items():
            with open(path, 'w') as f:
                f.write(code)
        self.package.reload()
        cachedproperty.reset(self)

    @cachedproperty    
    def changes(self):
        path = self._get_module_path(self.version1)
        with open(path) as f:
            lines = []
            for line in f:
                for name in self.version1.ORDER:
                    if line.strip().startswith(name):
                        line = line.replace(
                            str(getattr(self.version1, name)),
                            str(getattr(self.version2, name))
                        )
                        break
                lines.append(line)
            code = ''.join(lines)
        return {path: code}    
    
    @cachedproperty    
    def version1(self):
        return self.package.version
        
    @cachedproperty
    def version2(self):
        Version = type('Version', (self.version1.__class__,), {})
        if self.level:
            Version.LEVEL = self.level       
        if self.step == 'major':
            Version.MAJOR = Version.MAJOR+1
            Version.MINOR = 0
            Version.MICRO = 0
        elif self.step == 'minor':
            Version.MINOR = Version.MINOR+1
            Version.MICRO = 0
        elif self.step == 'micro':
            Version.MICRO = Version.MICRO+1 
        return Version()

    @staticmethod
    def _get_module_path(obj):
        return (sys.modules[obj.__module__].__file__.
                replace('.pyc', '.py'))