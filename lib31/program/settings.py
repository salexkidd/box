class Settings(dict):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                if not callable(value):
                    self[name] = value