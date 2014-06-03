from ..copy import enhanced_copy

def merge_dicts(dict1, dict2, *, mergers={}):
    """Recursively merge dicts and return new one.
    
    :param dict dict1: left dict to merge
    :param dict dict2: right dict to merge
    :param dict mergers: map of mergers by types
    
    :returns dict: merged dict
    """
    mergers.setdefault(dict, merge_dicts)
    result = enhanced_copy(dict1)
    for key in dict2:
        value = dict2[key]
        if key in dict1:
            value1 = dict1[key]
            value2 = dict2[key]
            type1 = type(value1)
            type2 = type(value2)
            if type1 == type2:
                merger = mergers.get(type1, None)
                if merger:
                    value = merger(value1, value2)
        result[key] = value
    return result