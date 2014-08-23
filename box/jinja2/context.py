class ObjectContext(dict):
    """Adapter between standard mapping context and object.

    Parameters
    ----------
    obj: object
        Object to adapt.
    kwargs: dict
        Standard dict items.
    """

    # Public

    def __init__(self, obj, **kwargs):
        self._object = obj
        self.update(**kwargs)

    def __contains__(self, key):
        if super().__contains__(key):
            return True
        else:
            return hasattr(self._object, key)

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            try:
                return getattr(self._object, key)
            except AttributeError:
                raise KeyError(key)

    def __copy__(self):
        context = type(self)(self._object)
        context.update(self)
        return context
