class Canvas:

    # Puplic

    def __init__(self, **kwargs):
        vars(self).update(kwargs)

    def __getattribute__(self, name):
        value = super().__getattribute__(name)
        if isinstance(value, str):
            value = value.format_map(self)
        return value

    def __getitem__(self, key):
        value = getattr(self, key)
        return value
