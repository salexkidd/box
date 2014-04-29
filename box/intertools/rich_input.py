from ..functools import FunctionCall

class rich_input(FunctionCall):
    
    #Public
    
    prompt = 'Input'
    separator = ': '
    default = None
    options = None
    attempts = 3
    error = 'Try again..'
    hint_indent = ' '
    hint_borders = '[]'
    hint_separator = '/'
    hint_on_default = staticmethod(str.upper)
    input_function = staticmethod(input)
    print_function = staticmethod(print)
    
    def __init__(self, prompt=None, **kwargs):
        if prompt != None:
            self.prompt = prompt
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def __call__(self):
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
        hint = ''
        if self.options:
            hint = ('{hint_indent}{hint_left_border}'
                    '{formatted_options}{hint_right_border}')
        elif self.default:
            hint = ('{hint_indent}{hint_left_border}'
                    '{formatted_default}{hint_right_border}')
        return '{prompt}'+hint+'{separator}'

    @property
    def templated_error(self):
        return '{error}'
    
    @property
    def context(self):
        context = {}
        for name in dir(self):
            if (name.startswith('rendered') or
                name.startswith('templated') or
                name.startswith('context')):
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
                    option = self.hint_on_default(option)
                elements.append(option)
            options = self.hint_separator.join(elements)
        return options
    
    @property
    def formatted_default(self):
        default = ''
        if self.default:
            default = self.default
        return default
    
    @property    
    def hint_left_border(self):
        return self.hint_borders[:int(len(self.hint_borders)/2)]
    
    @property    
    def hint_right_border(self):
        return self.hint_borders[int(len(self.hint_borders)/2):]