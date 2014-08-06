from ..copy import enhanced_copy


def merge_dicts(dict1, dict2, *, resolvers={}):
    """Recursively merge dicts and return new one.

    :param dict dict1: left dict to merge
    :param dict dict2: right dict to merge
    :param dict resolvers: resolvers by type

    :returns dict: merged dict
    """
    resolvers.setdefault(dict, merge_dicts)
    result = enhanced_copy(dict1)
    for key in dict2:
        value = dict2[key]
        if key in dict1:
            resolver1 = resolvers.get(type(dict1[key]), None)
            resolver2 = resolvers.get(type(dict2[key]), None)
            if resolver1 == resolver2 is not None:
                value = resolver1(dict1[key], dict2[key])
        result[key] = value
    return result
