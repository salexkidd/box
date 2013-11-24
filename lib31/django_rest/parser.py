from .exceptions import ConstraintsAreNotSuppported

class Parser:
    
    #Public
    
    def parse(self, constraints):
        result = {}
        if constraints:
            groups = constraints.split(';')
            for group in groups:
                try:
                    name, value = group.split('=')
                    result[name] = self.__process_value(name, value)
                except ValueError:
                    raise ConstraintsAreNotSuppported(constraints)
        return result
    
    #Private
 
    @staticmethod   
    def __process_value(name, value):
        try:
            if not value:
                raise Exception() 
            if name in []:
                return str(value)
            else:
                return int(value)
        except Exception:
            raise ValueError()