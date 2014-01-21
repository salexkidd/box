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
    
    default_prompt = 'Input'
    default_error = 'Try again..'
    default_attempts = 3 
    default_brackets = '[]'
    default_separator = '/'
    default_colon = ':'
    default_on_default = str.upper
    default_input_function = staticmethod(input)
    default_print_function = staticmethod(print)
    
    def __init__(self, prompt=None, error=None,
                 default=None, options=None, attempts=None,
                 formatted_prompt=None, formatted_error=None,
                 brackets=None, separator=None, colon=None, on_default=None,
                 input_function=None, print_function=None):
        self._prompt = prompt or self.default_prompt
        self._error = error or self.default_error
        self._default = default
        self._options = options
        self._attempts = attempts or self.default_attempts
        self._formatted_prompt = formatted_prompt
        self._formatted_error = formatted_error
        self._brackets = brackets if brackets != None else self.default_brackets
        self._separator = separator if separator != None else self.default_separator
        self._colon = colon if colon != None else self.default_colon
        self._on_default = on_default if on_default != None else self.default_on_default
        self._input_function = input_function or self.default_input_function
        self._print_function = print_function or self.default_print_function
        
    def execute(self):
        for _ in range(0, self._attempts):
            result = self._input_function(self._rendered_prompt)
            if not result:
                result = self._default
            if self._options:
                if result not in self._options:
                    self._print_function(self._rendered_error)
                    continue 
            return result
        else:
            raise ValueError(
                'Input error in all of {attempts} attempts '
                'where options are "{options}"'.format(
                    attempts=self._attempts,
                    options=self._options))       
    
    #Protected

    @property
    def _rendered_prompt(self):
        pass
    
    @property
    def _rendered_error(self):
        pass
    
    @property
    def _formatted_prompt(self):                                 
        prompt = self._prompt
        if self._options:
            options = []
            for option in self._options:
                if option == self._default:
                    option = self._on_default(option)
                options.append(option)
            options = self._separator.join(self._options)
        prompt = prompt+self._colon 
        return prompt  

    @property
    def _formatted_error(self):
        return self._error
    
    @property
    def _context(self):
        return {'prompt': self._prompt,
                'error': self._error,
                'default': self._default,
                'options': self._options,
                'attempts': self._attempts}      
    
    
locals().update({'input': Input()}) 