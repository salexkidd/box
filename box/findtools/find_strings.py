from functools import partial
from ..functools import Function, cachedproperty
from ..importlib import inject
from ..itertools import map_reduce
from ..os import enhanced_join
from ..types import RegexCompiledPatternType
from .find_files import FindFilesEmitter, find_files
from .not_found import NotFound


class find_strings(Function):
    """Find strings in files using map_reduce framework.

    :param str/re string: include string pattern
    :param list filters: find filters
    :param str basedir: base directory to find
    :param list filepathes: list of filepathes or globs where to find
    :param dict params: map_reduce params

    :returns mixed: map_reduce result
    """

    # Public

    default_emitter = inject('FindStringsEmitter', module=__name__)
    default_getfirst_exception = NotFound

    def __init__(self, *filters, string=None,
                 basedir=None, filepathes=None, **params):
        params.setdefault('emitter', self.default_emitter)
        params.setdefault(
            'getfirst_exception',
            self.default_getfirst_exception)
        self._string = string
        self._filters = filters
        self._basedir = basedir
        self._filepathes = filepathes
        self._params = params

    def __call__(self):
        objects = self._map_reduce(self._values, **self._params)
        return objects

    # Protected

    _find_files = staticmethod(find_files)
    _map_reduce = map_reduce
    _open = staticmethod(open)

    @cachedproperty
    def _values(self):
        for filepath in self._effective_filepathes:
            # Reads every file in filepathes
            full_filepath = enhanced_join(self._basedir, filepath)
            partial_emitter = partial(
                self._params['emitter'],
                filepath=filepath, basedir=self._basedir)
            with self._open(full_filepath) as fileobj:
                filetext = fileobj.read()
                if isinstance(self._string, RegexCompiledPatternType):
                    # Search string is regex object - re search
                    for match in self._string.finditer(filetext):
                        matched_groups = match.groups()
                        if matched_groups:
                            # Emits every matched group
                            for matched_group in matched_groups:
                                yield partial_emitter(matched_group)
                        else:
                            # Emits whole match
                            matched_string = match.group()
                            yield partial_emitter(matched_string)
                elif self._string:
                    # Search string is string - str search
                    matches = filetext.count(self._string)
                    for _ in range(matches):
                        # Emits given strings matches count times
                        yield partial_emitter(self._string)
                else:
                    # Search string is None - no search
                    # Emits whole file
                    yield partial_emitter(filetext)

    @cachedproperty
    def _effective_filepathes(self):
        filepathes = self._find_files(
            *self._filters,
            basedir=self._basedir,
            filepathes=self._filepathes)
        return filepathes


class FindStringsEmitter(FindFilesEmitter):
    """Emitter representation for find_strings.

    Additional attributes:

    - filepath
    - basedir
    """

    # Public

    pass
