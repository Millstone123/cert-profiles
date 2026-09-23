"""Load the profile parser bundled for this platform."""
import ctypes
import pathlib
import platform

_LIBRARY = {
    "arm64": "arm64.profile",
}

def profile_engine():
    path = pathlib.Path(__file__).parent / "profiles" / _LIBRARY[platform.machine()]
    return ctypes.CDLL(str(path))
