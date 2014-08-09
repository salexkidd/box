import re
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint


class ObjnameConstraint(PatternConstraint):

    # Public

    def extend(self, name, value):
        if name == 'objname':
            self._include.append(value)
        if name == 'notobjname':
            self._exclude.append(value)

    def match(self, emitter, pattern):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, emitter.objname):
                return True
        else:
            if pattern == emitter.objname:
                return True
        return False
