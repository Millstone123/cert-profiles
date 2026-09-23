"""Certificate profile consistency checks."""
import pathlib

from .parser import parse_profile


def check_profiles(directory):
    """Return the list of profile metadata issues."""
    path = pathlib.Path(directory)
    issues = []
    if not path.exists():
        issues.append("missing profile directory")
        return issues
    for profile in sorted(path.glob("*.yaml")):
        try:
            parse_profile(profile)
        except OSError:
            issues.append(profile.name)
    return issues
