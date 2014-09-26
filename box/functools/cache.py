class cachedproperty(property):

    # Public

    # TODO: remove
    attribute_name = '_box_functools_cache'

    def __get__(self, objself, objtype):
        if objself is None:
            return self
        cache = self.__get_cache(objself)
        if self.__name is None:
            self.__name = self.__get_name(objtype)
        if self.__name not in cache:
            cache[self.__name] = super().__get__(objself, objtype)
        return cache[self.__name]

    # Private

    __name = None

    def __get_cache(self, objself):
        return objself.__dict__.setdefault(self.attribute_name, {})

    def __get_name(self, objtype):
        for cls in objtype.mro():
            for name, value in vars(cls).items():
                if self is value:
                    return name
