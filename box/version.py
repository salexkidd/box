class Version(str):
    """Version representation.
    
    :param dict kwargs: key=value pairs to override version c 
    
    >>> from box import Version
    >>> class Version(Version):
    ...   major = 1
    ...   minor = 2
    ...   micro = 3
    ...
    >>> v = Version(micro=5)
    >>> v
    '1.2.5'
    >>> v.major
    1
    >>> v.info
    (1, 2, 5, 'final', 0)
    
    .. seealso:: Python versioning: `sys.version_info <https://docs.python.org/3/library/sys.html#sys.version_info>`_
    """
    
    #Public
    
    major = 0
    """Version's major component.
    """
    minor = 0
    """Version's minor component.
    """    
    micro = 0
    """Version's micro component.
    """    
    level = 'final'
    """Version's level.
    """
    serial = 0
    """Version's serial.
    """    
      
    def __new__(cls, version=None, **kwargs):
        if not version:
            version = str.__new__(cls)
        vars(version).update(kwargs)
        return str.__new__(cls, version._as_str)
    
    @property
    def info(self):
        """Version as a tuple.
        """
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
    
    
version = Version(major=0, minor=21, micro=1, level='final')