class BadRequest(Exception): pass
class VersionIsNotSuppported(BadRequest): pass
class FormatIsNotSuppported(BadRequest): pass
class ResourceIsNotSuppported(BadRequest): pass
class ConstraintsAreNotSuppported(BadRequest): pass