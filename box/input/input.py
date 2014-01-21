class Input:
    
    #Public
        
    def __call__(self, *args, **kwargs):
        call = self._call_class(*args, **kwargs)
        result = call.execute()
        return result
    
    #Protected
    
    _call_class = property(lambda self: InputCall)
    

class InputCall:
    
    #Public
    
    prompt = 'Input'
    error = 'Try again..'
    default = None
    options = None
    attempts = 3 
    brackets = '[]'
    separator = '/'
    colon = ':'
    on_default = staticmethod(str.upper)
    input_function = staticmethod(input)
    print_function = staticmethod(print)
    
    def __init__(self, prompt=None, **kwargs):
        if prompt != None:
            kwargs['prompt'] = prompt
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def execute(self):
        for _ in range(0, self.attempts):
            result = self.input_function(self.rendered_prompt)
            if not result:
                result = self.default
            if self.options:
                if result not in self.options:
                    self.print_function(self.rendered_error)
                    continue 
            return result
        else:
            raise ValueError(
                'Input error in all of {attempts} attempts '
                'where options are "{options}"'.format(
                    attempts=self.attempts,
                    options=self.options))
    
    @property
    def rendered_prompt(self):
        return self.templated_prompt.format(**self.context)
    
    @property
    def rendered_error(self):
        return self.templated_error.format(**self.context)
    
    @property
    def templated_prompt(self):                                 
        if self.options:
            return '{prompt} {left_bracket}{formatted_options}{right_bracket}{colon}'
        elif self.default:
            return '{prompt} {left_bracket}{formatted_default}{right_bracket}{colon}'
        else:
            return '{prompt}{colon}'

    @property
    def templated_error(self):
        return '{error}'
    
    @property
    def context(self):
        context = {}
        for name in dir(self):
            if name.startswith('rendered'):
                continue
            if name.startswith('templated'):
                continue
            if name.startswith('context'):
                continue            
            attr = getattr(self, name)
            if callable(attr):
                continue
            context[name] = attr
        return context
    
    @property
    def formatted_options(self):
        options = ''
        if self.options:
            elements = []
            for option in self.options:
                if option == self.default:
                    option = self.on_default(option)
                elements.append(option)
            options = self.separator.join(elements)
        return options
    
    @property
    def formatted_default(self):
        default = ''
        if self.default:
            default = self.default
        return default
    
    @property    
    def left_bracket(self):
        return self.brackets[:int(len(self.brackets)/2)]
    
    @property    
    def right_bracket(self):
        return self.brackets[int(len(self.brackets)/2):]    
    
    
locals().update({'input': Input()}) 