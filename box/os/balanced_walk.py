import os
from .enhanced_join import enhanced_join


def balanced_walk(dirpath=None, *,
                  basedir=None, mode=None, sorter=None):
    """Recursevly yield (dirpathes, filepathes) tuple
    level by level from top to bottom of directory tree.

    Parameters
    ----------
    dirpath: str
        Directory path or list of pathes.
    mode: str[files/dirs]
        Special yielding mode.
    basedir: str
        All pathes are relative to basedir.
    sorter: function(pathes)
        Function to sort pathes.

    Returns
    -------
    generator
        Generator of (dirpathes, filepathes) tuples.

    Notes
    -----
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
