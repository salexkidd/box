from ..functools import Function


class enhanced_input(Function):
    """Read a string from standard input.

    :param str prompt: default prompt
    :param dict kwargs: key=value parameter pairs

    When you called function with any kwarg it overrides class attributes
    and changes function behaviour. See parameter list below. All of them
    you can use in function call. Also all of them you can redefine in
    inherited class.
    """

    # Public

    prompt = 'Input'
    """Default prompt.
    """
    separator = ': '
    """Symbols to end prompt.
    """
    default = None
    """Default value if user will not input anything.
    """
    options = None
    """List of available options.
    """
    attempts = 3
    """How many attempts user have to match one of the available option.
    """
    error = 'Try again..'
    """Print when user fails to match one of the available option.
    """
    hint_indent = ' '
    """Indent before hint.
    """
    hint_borders = '()'
    """Borders around hint.
    """
    hint_separator = '/'
    """Separator to separate available options.
    """
    hint_on_default = staticmethod(lambda option: '[' + option + ']')
    """Function called on default value in available options.
    """
    input = staticmethod(input)
    """Base input function. For example you can use getpass.getpass.
    """
    print = staticmethod(print)
    """Base print function. For example you can use pprint.pprint.
    """

    def __init__(self, prompt=None, **kwargs):
        if prompt is not None:
            self.prompt = prompt
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __call__(self):
        for _ in range(0, self.attempts):
            result = self.input(self.rendered_prompt)
            if not result:
                result = self.default
            if self.options:
                if result not in self.options:
                    self.print(self.rendered_error)
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
        """Exactly what will be printed to user as prompt.
        """
        return self.templated_prompt.format(**self.context)

    @property
    def rendered_error(self):
        """Exactly what will be printed to user as error.
        """
        return self.templated_error.format(**self.context)

    @property
    def templated_prompt(self):
        """Prompt template.
        """
        hint = ''
        if self.options:
            hint = ('{hint_indent}{hint_left_border}'
                    '{formatted_options}{hint_right_border}')
        elif self.default:
            hint = ('{hint_indent}{hint_left_border}'
                    '{formatted_default}{hint_right_border}')
        return '{prompt}' + hint + '{separator}'

    @property
    def templated_error(self):
        """Error template.
        """
        return '{error}'

    @property
    def context(self):
        """Context to make rendered_* from templated_*.
        """
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
        """Options as a string.
        """
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
        """Default as a string.
        """
        default = ''
        if self.default:
            default = self.default
        return default

    @property
    def hint_left_border(self):
        """Left border for hint.
        """
        return self.hint_borders[:int(len(self.hint_borders) / 2)]

    @property
    def hint_right_border(self):
        """Right border for hint.
        """
        return self.hint_borders[int(len(self.hint_borders) / 2):]
