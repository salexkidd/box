from abc import ABCMeta, abstractmethod


class Constraint(metaclass=ABCMeta):

    # Public

    @abstractmethod
    def __call__(self, emitter):
        pass  # pragma: no cover

    @abstractmethod
    def __bool__(self):
        pass  # pragma: no cover

    @abstractmethod
    def extend(self, name, value):
        pass  # pragma: no cover


class CompositeConstraint(Constraint, metaclass=ABCMeta):

    # Public

    def __init__(self):
        self._include = []
        self._exclude = []

    def __bool__(self):
        return bool(self._include or self._exclude)

    def __repr__(self):
        return ('Include: {include}, exclude: {exclude}'.
                format(include=self._include,
                       exclude=self._exclude))


class PatternConstraint(CompositeConstraint, metaclass=ABCMeta):

    # Public

    def __call__(self, emitter):
        for pattern in self._include:
            if not self._match(emitter, pattern):
                emitter.skip()
        for pattern in self._exclude:
            if self._match(emitter, pattern):
                emitter.skip()

    # Protected

    @abstractmethod
    def _match(self, emitter, pattern):
        pass  # pragma: no cover
