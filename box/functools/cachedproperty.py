class cachedproperty:

    # Public

    attribute_name = '_box_functools_cached_properties'

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self._fget = fget
        self._fset = fset
        self._fdel = fdel
        self._doc = doc

    def __get__(self, obj, cls):
        if self._fget:
            cache = self.__get_object_cache(obj)
            if self.__name not in cache:
                cache[self.__name] = self._fget(obj)
            return cache[self.__name]
        else:
            raise AttributeError('Can\'t get attribute')

    def __set__(self, obj, value):
        if self._fset:
            self._fset(obj, value)
        else:
            raise AttributeError('Can\'t set attribute')

    def __delete__(self, obj):
        if self._fdel:
            self._fdel(obj)
        else:
            raise AttributeError('Can\'t delete attribute')

    @property
    def __doc__(self):
        if self._doc:
            return self._doc
        elif self._fget:
            return self._fget.__doc__
        else:
            return None

    def getter(self, fget):
        self._fget = fget
        return self

    def setter(self, fset):
        self._fset = fset
        return self

    def deleter(self, fdel):
        self._fdel = fdel
        return self

    @classmethod
    def set(cls, obj, name, value):
        cache = cls.__get_object_cache(obj)
        cache[name] = value

    @classmethod
    def reset(cls, obj, name):
        cache = cls.__get_object_cache(obj)
        cache.pop(name, None)

    # Private

    @property
    def __name(self):
        return self._fget.__name__

    @classmethod
    def __get_object_cache(cls, obj):
        return obj.__dict__.setdefault(cls.attribute_name, {})
