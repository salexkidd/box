from importlib.machinery import SourceFileLoader


def import_file(filepath):
    """Import module from file by filepath.

    Parameters
    ----------
    filepath: str
        Module filepath.

    Returns
    -------
    object
        Imported module.
    """
    loader = SourceFileLoader(filepath, filepath)
    # TODO: load_module is deprecated?
    module = loader.load_module(filepath)
    return module
