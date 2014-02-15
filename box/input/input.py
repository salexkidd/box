from ..functools import FunctionCall

class InputCall(FunctionCall):
    
    #Public
    
    prompt = 'Input'
    error = 'Try again..'
    default = None
    options = None
    attempts = 3 
    space = ' '
    brackets = '[]'
    end = ':'
    separator = '/'    
    on_default = staticmethod(str.upper)
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
            hint = '{space}{left_bracket}{formatted_options}{right_bracket}'
        elif self.default:
            hint = '{space}{left_bracket}{formatted_default}{right_bracket}'
        return '{prompt}'+hint+'{end}'

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
    
    
locals().update({'input': InputCall}) 