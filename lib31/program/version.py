class Version(str):
    
    #Public
        
    def __new__(cls):
        substrings = []
        for name in cls._elements:
            try:
                value = getattr(cls, name)
            except AttributeError:
                raise NotImplementedError(
                    'You have to implement all of version '
                    'elements: '+str(cls._elements)
                )
            substrings.append(cls._build_substring(name, value))
        return str.__new__(cls, cls._build_string(substrings))       
    
    @property
    def info(self):
        """
        Returns version tuple
        """
        return tuple(
            getattr(self, name) for name in self._elements
        )
        
    #Protected
    
    _elements = [
        'major',
        'minor',
        'micro',
        'level',
    ]
    
    @classmethod
    def _build_substring(cls, name, value):
        result = str(value)
        if name == 'level' and value == 'final':
            result = ''
        return result

    @classmethod
    def _build_string(cls, substrings):
        return '.'.join(item for item in substrings if item)