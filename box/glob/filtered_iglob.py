import os
import glob

def filtered_iglob(pattern, *, 
                   basedir=None, sorter=None, files=False, dirs=False):
    """Yield the paths matching a pattern using filters.
    
    :param str pattern: glob path pattern
    :param str basedir: pathname basedirs
    :param bool files: include files flag
    :param bool dirs: include dirs flag
    
    :returns object: paths generator
    
    Function doesn't support symbolic links.
    """
    if basedir != None:
        pattern = os.path.join(basedir, pattern)
    pathes = glob.iglob(pattern)
    if sorter != None:
        pathes = sorter(pathes)
    for path in pathes:
        if os.path.islink(path):
            continue
        if os.path.isfile(path) and not files:
            continue
        if os.path.isdir(path) and not dirs: 
            continue
        yield path