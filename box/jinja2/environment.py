from .template import TemplateMixin

class EnvironmentMixin:

    #Public
    
    @property
    def template_class(self):
        from jinja2 import Template
        class Template(TemplateMixin, Template): pass
        return Template