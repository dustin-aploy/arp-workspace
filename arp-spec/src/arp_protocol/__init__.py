"""ARP protocol package.

This package exposes protocol version metadata and packaged schema assets for
other workspace components. It intentionally does not implement runtime,
adapter, or certification execution behavior.
"""

from .version import PROTOCOL_VERSION, __version__

__all__ = ["PROTOCOL_VERSION", "__version__"]
