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
    
    def __init__(self, prompt, error=None, 
                 default=None, options=None, attempts=None,
                 input_function=None, print_function=None):
        self._prompt = prompt
        self._error = error or self._default_error
        self._default = default
        self._options = options
        self._attempts = attempts or self._default_attempts
        self._input_function = input_function or self._default_input_function
        self._print_function = print_function or self._default_print_function
        
    def execute(self):
        for _ in range(0, self._attempts):
            result = self._input_function(self._prompt)
            if not result:
                result = self._default
            if self._options:
                if result not in self._options:
                    self._print_function(self._error)
                    continue 
            return result
        else:
            raise ValueError(
                'Input error in all of {attempts} attempts '
                'where options are "{options}"'.format(
                    attempts=self._attempts,
                    options=self._options))       
    
    #Protected
    
    _default_error = 'Try again..'    
    _default_attempts = 3    
    _default_input_function = staticmethod(input)
    _default_print_function = staticmethod(print)
    
    @property
    def _rendered_prompt(self):
        template = self._template_class(self._prompt_template)
        prompt = template.render(self._context)
        return prompt

    @property
    def _rendered_error(self):
        template = self._template_class(self._error_template)
        error = template.render(self._context)
        return error
    
    @property
    def _context(self):
        return {'default': self._default,
                'options': self._options,
                'attempts': self._attempts}
        
    @property
    def _template_class(self):
        from jinja2 import Template
        return Template
    
    
locals().update({'input': Input()}) 