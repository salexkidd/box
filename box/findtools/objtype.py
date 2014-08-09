from .constraint import PatternConstraint


class ObjtypeConstraint(PatternConstraint):

    # Public

    def extend(self, name, value):
        if name == 'objtype':
            self._include.append(value)
        if name == 'notobjtype':
            self._exclude.append(value)

    def match(self, emitter, pattern):
        types = pattern
        if isinstance(types, type):
            types = [types]
        if isinstance(emitter.object, tuple(types)):
            return True
        return False
