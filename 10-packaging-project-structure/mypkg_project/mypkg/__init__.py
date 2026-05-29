"""mypkg - a minimal example package.

__init__.py marks a directory as a package and controls what's exposed
when someone does `from mypkg import ...`.
"""

from .greetings import greet

__all__ = ["greet"]
__version__ = "0.1.0"
