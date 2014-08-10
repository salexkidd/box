from functools import partial
from ..functools import cachedproperty
from ..os import enhanced_join
from ..types import RegexCompiledPatternType
from .emitter import StringEmitter
from .find import find
from .find_files import find_files


class find_strings(find):
    """Find strings in files using map_reduce framework.

    :param str/re string: include string pattern
    :param list filters: find filters
    :param str basedir: base directory to find
    :param list filepathes: list of filepathes or globs where to find
    :param dict params: map_reduce params

    :returns mixed: map_reduce result
    """

    # Public

    default_emitter = StringEmitter

    def __init__(self, *, string=None,
                 basedir=None, filepathes=None, **find_params):
        self._string = string
        self._basedir = basedir
        self._filepathes = filepathes
        super().__init__(**find_params)

    # Protected

    _find_files = staticmethod(find_files)
    _open = staticmethod(open)

    @cachedproperty
    def _values(self):
        for filepath in self._effective_filepathes:
            # Reads every file in filepathes
            full_filepath = enhanced_join(self._basedir, filepath)
            partial_emitter = partial(
                self._emitter, basedir=self._basedir, filepath=filepath)
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
            basedir=self._basedir,
            filepathes=self._filepathes,
            filters=self._effective_filters)
        return filepathes
