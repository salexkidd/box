import os


def enhanced_join(*components, skip_none=True, fallback=None):
    """Enhanced version of os.path.join.

    Parameters
    ----------
    component: str
        Path component to join.
    kip_none: bool s
        Skip if None in components.
    fallback: mixed
        If join fails return fallback.

    Returns
    -------
    str
        Joined path.
    """
    try:
        if skip_none:
            components = filter(
                lambda component: component is not None, components)
        return os.path.join(*components)
    except Exception:
        if fallback is not None:
            return fallback
        else:
            raise
