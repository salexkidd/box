class Version(str):
    
    #Public
    
    major = 0
    minor = 0
    micro = 0
    level = 'final'
    serial = 0
      
    def __new__(cls, version=None):
        if not version:
            version = str.__new__(cls)
        return str.__new__(cls, version._as_string)
    
    @property
    def info(self):
        return self._as_tuple
    
    #Protected
              
    @property
    def _as_tuple(self):
        return (self.major, self.minor, self.micro, self.level, self.serial)
    
    @property
    def _as_string(self):
        items = [self.major, self.minor, self.micro] 
        if self.level != 'final':
            items.append(self.level)
        return '.'.join(map(str, items)) 