import operator
from ..collections import merge_dicts
from ..package import Settings


class Settings(Settings):
    """Settings with argparse config.
    """

    # Public

    @property
    def argparse(self):
        return {}

    # Protected

    # TODO: replace by DerivedDict?
    def _inherit_argparse(self, current_class, extension):
        base = getattr(super(current_class, self), 'argparse', {})
        return merge_dicts(base, extension, resolvers={list: operator.add})
