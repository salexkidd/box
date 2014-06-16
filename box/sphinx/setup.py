def setup(method):
    """Decorate method to be added to sphinx setup.
    """
    method._box_setup = True
    return method