from .constraint import PatternConstraint

class ObjtypeConstraint(PatternConstraint):
    
    #Protected
        
    def _match(self, pattern, emitter):
        types = pattern
        if isinstance(types, type):
            types = [types]
        if isinstance(emitter.object, tuple(types)):
            return True
        return False