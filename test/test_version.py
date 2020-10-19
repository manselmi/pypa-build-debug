# stdlib imports
import importlib
import sys

# third-party imports
from packaging.version import Version

# first-party imports
import pypa_build_debug


Distribution = (
    importlib.import_module('importlib.metadata')
    if sys.version_info >= (3, 8) else
    importlib.import_module('importlib_metadata')
).Distribution


def test_version():
    module = pypa_build_debug
    dist = Distribution.from_name(module.__package__)
    version = str(Version(dist.version))  # asserts PEP 440 compliance
    assert version == module.__version__
