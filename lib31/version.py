import sys 

class Version(str):
    
    #Current
    MAJOR = 0
    MINOR = 1
    MICRO = 0
    LEVEL = 'final'

    #Order
    ORDER = [
        'MAJOR', 
        'MINOR',
        'MICRO', 
        'LEVEL',
    ]
    
    #Base
    BASE = None
        
    def __new__(cls):
        elements = []
        for name in cls.ORDER:
            value = str(getattr(cls, name))
            if value != 'final':
                elements.append(value)
        return str.__new__(cls, '.'.join(elements))
    
    @property
    def info(self):
        return tuple(getattr(self, name) 
                     for name in self.ORDER)
    
    @property
    def path(self):
        if not self.BASE:            
            name = self.__module__
        else:
            name = self.BASE.__module__
        return sys.modules[name].__file__.replace('.pyc', '.py')
    
    @property
    def code(self):
        with open(self.path) as f:
            if not self.BASE:
                return f.read()
            else:
                lines = []
                for line in f:
                    for name in self.ORDER:
                        if line.strip().startswith(name):
                            line = line.replace(
                                str(getattr(self.BASE, name)),
                                str(getattr(self, name))
                            )
                            break
                    lines.append(line)
                return ''.join(lines)
                

    def next(self, step='minor', level='final'):
        Version = type('Version', (self.__class__,), {})                
        Version.LEVEL = level
        Version.BASE = self             
        if step == 'major':
            Version.MAJOR = self.MAJOR+1
            Version.MINOR = 0
            Version.MICRO = 0
        elif step == 'minor':
            Version.MINOR = self.MINOR+1
            Version.MICRO = 0
        elif step == 'micro':
            Version.MICRO = self.MICRO+1   
        return Version()  