import re
from ..types import RegexCompiledPatternType
from .constraint import PatternConstraint


class ObjnameConstraint(PatternConstraint):

    # Protected

    def _match(self, pattern, emitter):
        if isinstance(pattern, RegexCompiledPatternType):
            if re.search(pattern, emitter.objname):
                return True
        else:
            if pattern == emitter.objname:
                return True
        return False
