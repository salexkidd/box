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
    on_default = str.upper
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
        return self.formatted_prompt.format(self.context)
    
    @property
    def rendered_error(self):
        return self.formatted_error.format(self.context)
    
    @property
    def formatted_prompt(self):                                 
        prompt = self.prompt
        if self.options:
            options = []
            for option in self.options:
                if option == self.default:
                    option = self.on_default(option)
                options.append(option)
            options = self.separator.join(self.options)
        elif self.default:
            prompt = prompt+self.default
        prompt = prompt+self.colon 
        return prompt  

    @property
    def formatted_error(self):
        return self.error
    
    @property
    def context(self):
        return {'prompt': self.prompt,
                'error': self.error,
                'default': self.default,
                'options': self.options,
                'attempts': self.attempts}      
    
    
locals().update({'input': Input()}) 