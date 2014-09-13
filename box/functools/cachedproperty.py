class cachedproperty:

    # Public

    attribute_name = '_box_functools_cached_properties'

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.__fget = fget
        self.__fset = fset
        self.__fdel = fdel
        self.__doc = doc

    def __get__(self, obj, cls):
        if self.__fget:
            cache = self.__get_object_cache(obj)
            if self.__name not in cache:
                cache[self.__name] = self.__fget(obj)
            return cache[self.__name]
        else:
            raise AttributeError('Can\'t get attribute')

    def __set__(self, obj, value):
        if self.__fset:
            self.__fset(obj, value)
        else:
            raise AttributeError('Can\'t set attribute')

    def __delete__(self, obj):
        if self.__fdel:
            self.__fdel(obj)
        else:
            raise AttributeError('Can\'t delete attribute')

    @property
    def __doc__(self):
        if self.__doc:
            return self.__doc
        elif self.__fget:
            return self.__fget.__doc__
        else:
            return None

    def getter(self, fget):
        self.__fget = fget
        return self

    def setter(self, fset):
        self.__fset = fset
        return self

    def deleter(self, fdel):
        self.__fdel = fdel
        return self

    @classmethod
    def set(cls, obj, name, value):
        cache = cls.__get_object_cache(obj)
        cache[name] = value

    @classmethod
    def reset(cls, obj, name):
        cache = cls.__get_object_cache(obj)
        cache.pop(name, None)

    # Protected

    @property
    def __name(self):
        return self.__fget.__name__

    @classmethod
    def __get_object_cache(cls, obj):
        return obj.__dict__.setdefault(cls.attribute_name, {})
