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
    
    def __init__(self, prompt=None, error=None,
                 default=None, options=None, attempts=None,
                 formatted_prompt=None, formatted_error=None, 
                 input_function=None, print_function=None):
        self._prompt = prompt or self._default_prompt
        self._error = error or self._default_error
        self._default = default
        self._options = options
        self._attempts = attempts or self._default_attempts
        self._formatted_prompt = formatted_prompt or self._default_formatted_prompt
        self._formatted_error = formatted_error or self._default_formatted_error
        self._input_function = input_function or self._default_input_function
        self._print_function = print_function or self._default_print_function
        
    def execute(self):
        for _ in range(0, self._attempts):
            result = self._input_function(self._prepared_prompt)
            if not result:
                result = self._default
            if self._options:
                if result not in self._options:
                    self._print_function(self._prepared_error)
                    continue 
            return result
        else:
            raise ValueError(
                'Input error in all of {attempts} attempts '
                'where options are "{options}"'.format(
                    attempts=self._attempts,
                    options=self._options))       
    
    def format_prompt(self):
        return self._prompt+':'  

    def format_error(self):
        return self._error
    
    #Protected

    _default_prompt = 'Input'
    _default_error = 'Try again..'
    _default_attempts = 3 
    _default_formatted_prompt = staticmethod(format_prompt)
    _default_formatted_error = staticmethod(format_error)
    _default_input_function = staticmethod(input)
    _default_print_function = staticmethod(print)
     
    @property   
    def _prepared_prompt(self):
        prepared_prompt = self._formatted_prompt
        if callable(prepared_prompt):
            prepared_prompt = prepared_prompt(self)
        return prepared_prompt

    @property   
    def _prepared_error(self):
        prepared_error = self._formatted_error
        if callable(prepared_error):
            prepared_error = prepared_error(self)
        return prepared_error
    
    
locals().update({'input': Input()}) 