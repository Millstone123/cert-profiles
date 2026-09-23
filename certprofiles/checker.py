"""Certificate profile consistency checks."""
import pathlib


def check_profiles(directory):
    """Return the list of profile metadata issues."""
    path = pathlib.Path(directory)
    issues = []
    if not path.exists():
        issues.append("missing profile directory")
    return issues
