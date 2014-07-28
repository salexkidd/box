import os
from .enhanced_join import enhanced_join

def balanced_walk(dirpath=None, *,
                  basedir=None, mode=None, sorter=None):
    """Recursevly yield (dirpathes, filepathes) tuple
    level by level from top to bottom of directory tree.

    :param str dirpath: directory path or list of pathes
    :param str[files/dirs] mode: special yielding mode
    :param str basedir: all pathes are relative to basedir
    :param function(pathes) sorter: function to sort pathes

    :returns generator: (dirpathes, filepathes) generator

    Function doesn't support symbolic links.
    """
    dirpathes = dirpath
    if not isinstance(dirpath, list):
        dirpathes = [dirpath]
    inner_filepathes = []
    inner_dirpathes = []
    for dirpath in dirpathes:
        full_dirpath = enhanced_join(basedir, dirpath, fallback='.')
        for name in os.listdir(full_dirpath):
            path = enhanced_join(dirpath, name)
            full_path = enhanced_join(basedir, path)
            if os.path.islink(full_path):
                continue
            elif os.path.isfile(full_path):
                inner_filepathes.append(path)
            elif os.path.isdir(full_path):
                inner_dirpathes.append(path)
    if sorter is not None:
        inner_filepathes = sorter(inner_filepathes)
        inner_dirpathes = sorter(inner_dirpathes)
    if mode == 'files':
        yield from inner_filepathes
    elif mode == 'dirs':
        yield from inner_dirpathes
    else:
        yield (inner_dirpathes, inner_filepathes)
    if inner_dirpathes:
        yield from balanced_walk(
            inner_dirpathes,
            basedir=basedir,
            mode=mode,
            sorter=sorter)
