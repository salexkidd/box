class cachedproperty(property):

    # Public

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError('can\'t get attribute')
        name = self.__get_name(obj)
        cache = self.__get_cache(obj)
        if name not in cache:
            cache[self.__name] = self.fget(obj)
        return cache[self.__name]

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError('can\'t set attribute')
        name = self.__get_name(obj)
        cache = self.__get_cache(obj)
        self.fset(obj, cache, name, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError('can\'t delete attribute')
        name = self.__get_name(obj)
        cache = self.__get_cache(obj)
        self.fdel(obj, cache, name)

    # Private

    __name = None
    __cache = '_box_functools_cache'

    def __get_name(self, obj):
        if self.__name is None:
            for cls in type(obj).mro():
                for name, value in vars(cls).items():
                    if self is value:
                        self.__name = name
        return self.__name

    def __get_cache(self, obj):
        return obj.__dict__.setdefault(self.__cache, {})
