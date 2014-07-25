from abc import ABCMeta

class NullMetaclass(ABCMeta):
    """Metaclass making Null class acting like Null.
    """

    # Public

    def __bool__(self):
        return False

    def __repr__(self):
        return 'Null'

    def __instancecheck__(self, instance):
        result = issubclass(instance, self)
        if not result:
            result = super().__instancecheck__(instance)
        return result


class Null(metaclass=NullMetaclass):
    """Null value to use instead of None.
    """

    # Public

    pass
