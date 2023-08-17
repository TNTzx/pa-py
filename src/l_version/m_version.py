"""Contains the version base class."""

import typing as typ



class LevelData():
    """Represents level data."""


T = typ.TypeVar("T")
class Version(typ.Generic[T]):
    """Represents a PA version."""
    version_str: str
    level_data_cls: type[T]

    def __init__(self, level_data: T):
        self.level_data = level_data
