import os
import glob
from ..os import enhanced_join

def filtered_iglob(pattern, *, 
                   basedir=None, sorter=None, files=False, dirs=False):
    """Yield the paths matching a pattern using filters.
    
    :param str pattern: glob path pattern
    :param str basedir: all pathes are relative to basedir
    :param function(pathes) sorter: function to sort pathes
    :param bool files: include files flag
    :param bool dirs: include dirs flag
    
    :returns object: paths generator
    
    Function doesn't support symbolic links.
    """
    full_pattern = enhanced_join(basedir, pattern)
    full_pathes = glob.iglob(full_pattern)
    if sorter != None:
        full_pathes = sorter(full_pathes)
    for full_path in full_pathes:
        if os.path.islink(full_path):
            continue
        if os.path.isfile(full_path) and not files:
            continue
        if os.path.isdir(full_path) and not dirs: 
            continue
        path = os.path.relpath(full_path, start=basedir)
        yield path