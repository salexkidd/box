import os
import glob
from ..os import enhanced_join

def enhanced_iglob(pattern, *,
                   basedir=None, mode=None, sorter=None):
    """Yield the pathes matching the pattern.

    :param str pattern: glob path pattern
    :param str basedir: all pathes are relative to basedir
    :param str[files/dirs] mode: filtering mode
    :param function(pathes) sorter: function to sort pathes

    :returns object: paths generator

    Function doesn't support symbolic links.
    """
    full_pattern = enhanced_join(basedir, pattern)
    full_pathes = glob.iglob(full_pattern)
    if sorter is not None:
        full_pathes = sorter(full_pathes)
    for full_path in full_pathes:
        path = os.path.relpath(full_path, start=basedir)
        if os.path.islink(full_path):
            continue
        if mode == 'files':
            if os.path.isfile(full_path):
                yield path
        elif mode == 'dirs':
            if os.path.isdir(full_path):
                yield path
        else:
            yield path
