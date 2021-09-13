"""
The gpustat module.
"""

__version__ = '0.6.1post3.patched_for_manage_gpus'

from .core import GPUStat, GPUStatCollection
from .core import new_query
from .__main__ import print_gpustat, main


__all__ = (
    '__version__',
    'GPUStat', 'GPUStatCollection',
    'new_query',
    'print_gpustat', 'main',
)
