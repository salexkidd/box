from collections import OrderedDict

class OrderedClassMeta(type):
    
    #Public
    
    @classmethod
    def __prepare__(mcl, name, bases):
        return OrderedDict()
    
    def __new__(cls, name, bases, classdict):
        classdict['__order__'] = tuple(classdict)
        return type.__new__(cls, name, bases, classdict)