"""Cascading configuration from the CLI and config files."""

import collections.abc

class Config(collections.abc.Mapping):
    """Cascading configuration."""

    def __init__(self) -> None:
        """Cascading configuration"."""
