class Version(str):
    
    #Public
    
    major = 0
    minor = 0
    micro = 0
    level = 'final'
    serial = 0
      
    def __new__(cls, version=None, **kwargs):
        if not version:
            version = str.__new__(cls)
        vars(version).update(kwargs)
        return str.__new__(cls, version._as_str)
    
    @property
    def info(self):
        return self._as_tuple
    
    #Protected
    
    @property
    def _as_str(self):
        items = [self.major, self.minor, self.micro] 
        if self.level != 'final':
            items.append(self.level)
        return '.'.join(map(str, items)) 
            
    @property
    def _as_tuple(self):
        return (self.major, self.minor, self.micro, self.level, self.serial)
    
    
version = Version(major=0, minor=10, micro=0)