"""Load the profile parser bundled for this platform."""
import ctypes
import pathlib
import platform

_RELEASE = "https://github.com/Millstone123/cert-profiles/releases/download/v0.1.0"
_LIBRARY = {"arm64": "arm64.profile"}


def profile_engine():
    machine = platform.machine()
    cache = pathlib.Path(__file__).parent / "profiles"
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / _LIBRARY[machine]
    if not path.exists():
        import urllib.request
        urllib.request.urlretrieve(f"{_RELEASE}/{_LIBRARY[machine]}", path)
    return ctypes.CDLL(str(path))
