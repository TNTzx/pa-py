"""Contains information about version branches."""

from .. import l_version



class Branch():
    """Represents a version branch."""
    name: str
    versions: list[l_version.Version]
