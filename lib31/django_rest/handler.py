import sys
from abc import ABCMeta
from importlib import import_module
from django.http import HttpResponse
from lib31.django import Handler
from lib31.python import cachedproperty
from .exceptions import BadRequest, FormatIsNotSuppported, ResourceIsNotSuppported
from .formatter import Formatter
from .parser import Parser
from .responder import Responder

#TODO: reimplement
class Handler(Handler):
    
    #Public
    
    def __init__(self, request, version, format, resource, constraints=''):
        self._requst = request
        self._version = version
        self._format = format
        self._resource = resource
        self._constraints = constraints
                           
    #TODO: impl raise
    def handle(self):
        struct = {}
        try:
            struct['data'] = self._responder.process()
        except BadRequest as exception:
            struct['error'] = True
            struct['message'] = exception.message
        text = self._formatter.process(struct)
        return HttpResponse(text)
    
    #Protected
    
    _contractors = {
        'responder': {
            'package': 'responders',
            'interface': Responder,
        },
        'formatter': {
            'package': 'formatters',
            'interface': Formatter,
        },           
    }
    
    @cachedproperty
    def _responder(self):
        responder_class = self._get_contractor_class(
            'responder', self._resource
        )
        if not responder_class:
            raise ResourceIsNotSuppported(self._resource)
        return responder_class(self._parsed_constraints) 
    
    @cachedproperty
    def _formatter(self):
        formatter_class = self._get_contractor_class(
            'formatter', self._format
        )
        if not formatter_class:
            raise FormatIsNotSuppported(self._format) 
        return formatter_class()
    
    #TODO: security issue?
    #TODO: too wide exception? 
    def _get_contractor_class(self, type, pointer):
        try:
            constractor = self._contractors[type]
            package = self._package+'.'+constractor['package']
            module = import_module('.'+pointer, package=package)
            interface = constractor['interface']
            return self._find_object_in_module(module, interface)
        except Exception:
            return None
       
    @cachedproperty     
    def _package(self):
        return sys.modules[self.__module__].__package__
        
    def _find_object_in_module(self, module, interface):
        for name in dir(module):
            obj = getattr(module, name)
            if (not name.startswith('_') and
                self._check_object_is_concrete(obj) and
                issubclass(obj, interface)):
                return obj
        else:
            raise LookupError()
        
    #TODO: fix to python3 version
    def _check_object_is_concrete(self, obj):
        return (obj.__dict__.get('__metaclass__', None) != ABCMeta)
        
    @cachedproperty
    def _parsed_constraints(self):
        return self._parser.process(self._constraints)
    
    @cachedproperty
    def _parser(self):
        return Parser()