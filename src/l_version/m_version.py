"""Contains the version base class."""

from __future__ import annotations

import typing as typ
import abc



class LevelData():
    """Represents level data."""

class CombineSettings():
    """Represents combining settings."""

CombineSettingsT = typ.TypeVar("CombineSettingsT", CombineSettings)
class Level(typ.Generic[CombineSettingsT], abc.ABC):
    """Represents a PA level."""

    @classmethod
    @abc.abstractmethod
    def combine_levels(
        cls,
        levels: list[Level],
        primary_level: Level | None = None,
        combine_settings: CombineSettingsT = CombineSettings()
    ):
        """
        Combines levels into one level.
        If provided, the primary level will be combined to the other levels and will keep all properties regardless of the combine settings.
        """


class Version():
    """Represents a PA version."""
    version_str: str
    level_cls: type[Level]
