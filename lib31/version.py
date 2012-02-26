class Version(str):

    #Current
    MAJOR = 0
    MINOR = 1
    MICRO = 3
    LEVEL = 'final'
    
    #Order
    ORDER = [
        'MAJOR',
        'MINOR',
        'MICRO',
        'LEVEL',
    ]
        
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