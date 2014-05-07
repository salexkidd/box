import os

def enhanced_listdir(dirpath=None):
    """os.listdir explicit working with None dirpath.
    """
    if dirpath == None:
        return os.listdir()
    else:
        return os.listdir(dirpath)