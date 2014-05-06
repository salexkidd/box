import os
from glob import iglob

def filtered_iglob(pathname, files=False, dirs=False):
    """Yield the paths matching a pathname pattern.
    
    :param str pathname: glob pathname pattern
    :param bool files: include files flag
    :param bool dirs: include dirs flag
    
    :returns object: paths generator
    
    Function doesn't support symbolic links.
    """
    for path in iglob(pathname):
        if os.path.islink(path):
            continue
        if os.path.isfile(path) and files:
            continue
        if os.path.isdir(path) and dirs: 
            continue
        yield path