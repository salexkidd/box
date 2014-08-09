import os
from .constraint import Constraint


class MaxdepthConstraint(Constraint):

    # Public

    def __init__(self):
        self._maxdepth = None

    def __bool__(self):
        return (self._maxdepth is not None)

    def __extend__(self, name, value):
        if name == 'maxdepth':
            self._maxdepth = value

    def __call__(self, emitter):
        if self._maxdepth is not None:
            depth = emitter.filepath.count(os.path.sep) + 1
            if depth > self._maxdepth:
                emitter.skip()
                emitter.stop()
