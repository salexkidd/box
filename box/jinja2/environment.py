from .template import TemplateMixin

class EnvironmentMixin:
    """Mixin adds to jinja2.Environment template with :class:`TemplateMixin`.
    """

    #Public
    
    @property
    def template_class(self):
        from jinja2 import Template
        class Template(TemplateMixin, Template): pass
        return Template