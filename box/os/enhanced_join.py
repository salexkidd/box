import os

def enhanced_join(*components):
    """os.path.join working with None components.
    """
    components = filter(lambda component: component != None, components)
    return os.path.join(*components)